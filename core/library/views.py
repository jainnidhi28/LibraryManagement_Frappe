import requests
from decimal import Decimal
from django.utils import timezone
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book, Member, Transaction
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer, ImportBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  

    def get_serializer_class(self):
        if self.action == 'import_books':
            return ImportBookSerializer
        return BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query', '')
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query)
        )
        return Response(BookSerializer(books, many=True).data)

    @action(detail=False, methods=['post'])
    def import_books(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        count = serializer.validated_data.get('count', 20)
        title = serializer.validated_data.get('title', '')

        page = 1
        imported = 0

        while imported < count:
            url = f"https://frappe.io/api/method/frappe-library?page={page}&title={title}"
            response = requests.get(url)

            if response.status_code != 200:
                return Response({"error": "Failed to fetch from Frappe API"}, status=500)

            books = response.json().get("message", [])
            if not books:
                break

            for book in books:
                if imported >= count:
                    break
                try:
                    Book.objects.get(isbn=book['isbn'])
                    continue
                except Book.DoesNotExist:
                    Book.objects.create(
                        title=book['title'][:255],
                        authors=book['authors'][:255],
                        isbn=book['isbn'][:20],
                        publisher=book['publisher'][:255],
                        num_pages=int(book.get('num_pages') or 0),
                        stock=1
                    )
                    imported += 1
            page += 1

        return Response({"message": f"{imported} books imported successfully!"})


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['post'])
    def issue(self, request):
        member_id = request.data.get('member')
        book_id = request.data.get('book')
        issue_date = request.data.get('issue_date')

        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)
        except (Member.DoesNotExist, Book.DoesNotExist):
            return Response({"error": "Invalid book or member ID."}, status=400)

        if member.outstanding_debt > 500:
            return Response({"error": "Member has debt over ₹500."}, status=400)

        if book.stock < 1:
            return Response({"error": "Book not in stock."}, status=400)

        transaction = Transaction.objects.create(
            book=book,
            member=member,
            issue_date=issue_date or timezone.now().date()
        )

        book.stock -= 1
        book.save()

        return Response(TransactionSerializer(transaction).data, status=201)

    @action(detail=True, methods=['post'], url_path='return')  # ✅ THIS LINE IS UPDATED
    def return_book(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(id=pk)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found."}, status=404)

        if transaction.return_date:
            return Response({"error": "Book already returned."}, status=400)

        return_date = request.data.get('return_date')
        rent_fee = request.data.get('rent_fee')

        if not rent_fee:
            return Response({"error": "Rent fee is required."}, status=400)

        try:
            rent_fee = Decimal(rent_fee)
        except:
            return Response({"error": "Invalid rent fee."}, status=400)

        transaction.return_date = return_date or timezone.now().date()
        transaction.rent_fee = rent_fee
        transaction.save()

        book = transaction.book
        book.stock += 1
        book.save()

        member = transaction.member
        member.outstanding_debt += rent_fee
        member.save()

        return Response(TransactionSerializer(transaction).data)