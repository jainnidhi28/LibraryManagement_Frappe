<template>
  <div class="transaction-list-container">
    <h2>📋 All Transactions</h2>

    <router-link to="/transactions/issue">
      <button class="btn">➕ Issue Book</button>
    </router-link>

    <router-link to="/transactions/return">
      <button class="btn return">🔄 Return Book</button>
    </router-link>

    <table class="transaction-table">
      <thead>
        <tr>
          <th>Book</th>
          <th>Member</th>
          <th>Issue Date</th>
          <th>Return Date</th>
          <th>Rent Fee</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="tx in transactions" :key="tx.id">
          <td>{{ getBookTitle(tx.book) }}</td>
          <td>{{ getMemberName(tx.member) }}</td>
          <td>{{ tx.issue_date || '—' }}</td>
          <td>{{ tx.return_date || '—' }}</td>
          <td>₹{{ tx.rent_fee ?? '0.00' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TransactionList',
  data() {
    return {
      transactions: [],
      books: [],
      members: [],
    }
  },
  methods: {
    async fetchData() {
      const [txRes, booksRes, membersRes] = await Promise.all([
        axios.get('http://localhost:8000/api/transactions/'),
        axios.get('http://localhost:8000/api/books/'),
        axios.get('http://localhost:8000/api/members/'),
      ])
      this.transactions = txRes.data
      this.books = booksRes.data
      this.members = membersRes.data
    },
    getBookTitle(id) {
      const book = this.books.find((b) => b.id === id)
      return book?.title || 'Unknown'
    },
    getMemberName(id) {
      const member = this.members.find((m) => m.id === id)
      return member?.name || 'Unknown'
    },
  },
  created() {
    this.fetchData()
  },
}
</script>

<style scoped>
.transaction-list-container {
  max-width: 1000px;
  margin: 30px auto;
  background: white;
  padding: 20px;
  border-radius: 12px;
}

.btn {
  background: #4caf50;
  color: white;
  margin: 10px 10px 20px 0;
  padding: 10px 14px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.btn.return {
  background: #2196f3;
}
.transaction-table {
  width: 100%;
  border-collapse: collapse;
}
.transaction-table th,
.transaction-table td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}
.transaction-table th {
  background: #f5f5f5;
}
</style>
