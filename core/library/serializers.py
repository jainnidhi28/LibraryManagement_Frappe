from rest_framework import serializers
from .models import Book, Member, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(source='book.id', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)
    member_id = serializers.IntegerField(source='member.id', read_only=True)
    member_name = serializers.CharField(source='member.name', read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id', 'book', 'book_id', 'book_title',
            'member', 'member_id', 'member_name',
            'issue_date', 'return_date', 'rent_fee'
        ]
        
class ImportBookSerializer(serializers.Serializer):
    count = serializers.IntegerField(required=False, min_value=1)
    title = serializers.CharField(required=False, allow_blank=True)