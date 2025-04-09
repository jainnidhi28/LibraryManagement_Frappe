<template>
  <div class="form-container">
    <h2>📚 Issue Book</h2>
    <form @submit.prevent="issueBook">
      <div class="form-group">
        <label>Member</label>
        <select v-model="form.member" required>
          <option disabled value="">-- Select Member --</option>
          <option v-for="member in members" :key="member.id" :value="member.id">
            {{ member.name }} (₹{{ member.outstanding_debt }})
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Book</label>
        <select v-model="form.book" required>
          <option disabled value="">-- Select Book --</option>
          <option v-for="book in books" :key="book.id" :value="book.id">
            {{ book.title }} - Stock: {{ book.stock }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Issue Date</label>
        <input type="date" v-model="form.issue_date" />
      </div>

      <button type="submit">Issue Book</button>
    </form>

    <div v-if="message" class="message" :class="{ error }">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'IssueTransaction',
  data() {
    return {
      books: [],
      members: [],
      form: {
        member: '',
        book: '',
        issue_date: '',
      },
      message: '',
      error: false,
    }
  },
  async created() {
    const [bookRes, memberRes] = await Promise.all([
      axios.get('http://localhost:8000/api/books/'),
      axios.get('http://localhost:8000/api/members/'),
    ])
    this.books = bookRes.data
    this.members = memberRes.data
  },
  methods: {
    async issueBook() {
      this.message = ''
      this.error = false

      try {
        const payload = {
          member: this.form.member,
          book: this.form.book,
          issue_date: this.form.issue_date || null,
        }
        const res = await axios.post('http://localhost:8000/api/transactions/issue/', payload)
        this.message = `✅ Book issued successfully! Transaction ID: ${res.data.id}`
        this.form = { member: '', book: '', issue_date: '' }

        setTimeout(() => this.$router.push('/transactions'), 1000)
      } catch (err) {
        this.error = true
        this.message = err.response?.data?.error || '❌ Failed to issue book.'
      }
    },
  },
}
</script>

<style scoped>
.form-container {
  max-width: 600px;
  margin: 30px auto;
  background: #fff;
  padding: 20px;
  border-radius: 10px;
}

.form-group {
  margin-bottom: 15px;
}

select,
input[type='date'],
button {
  width: 100%;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

button {
  background-color: #4caf50;
  color: white;
  border: none;
}
button:hover {
  background-color: #388e3c;
}

.message {
  margin-top: 15px;
  padding: 10px;
  border-radius: 6px;
  font-weight: bold;
}
.message.error {
  background-color: #ffcdd2;
  color: #c62828;
}
.message:not(.error) {
  background-color: #c8e6c9;
  color: #2e7d32;
}
</style>
