<template>
  <div class="form-container">
    <h2>📥 Return Book</h2>

    <button class="back-button" @click="$router.push('/transactions')">
      ← Back to Transactions
    </button>

    <form @submit.prevent="returnBook">
      <div class="form-group">
        <label>Select Book</label>
        <select v-model="selectedBookId" required @change="updateMemberList">
          <option disabled value="">-- Select Issued Book --</option>
          <option v-for="book in uniqueBooks" :key="book.book_id" :value="book.book_id">
            {{ book.book_title }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Select Member</label>
        <select v-model="selectedMemberId" required @change="updateIssueDate">
          <option disabled value="">-- Select Member --</option>
          <option
            v-for="member in filteredMembers"
            :key="member.member_id"
            :value="member.member_id"
          >
            {{ member.member_name }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Issue Date</label>
        <input type="date" v-model="issueDate" readonly />
      </div>

      <div class="form-group">
        <label>Return Date</label>
        <input type="date" v-model="form.return_date" required />
      </div>

      <div class="form-group">
        <label>Rent Fee (₹)</label>
        <input type="number" v-model="form.rent_fee" step="0.01" min="0" required />
      </div>

      <button type="submit">Return Book</button>
    </form>

    <div v-if="message" class="message" :class="{ error }">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReturnBook',
  data() {
    return {
      activeTransactions: [],
      selectedBookId: '',
      selectedMemberId: '',
      issueDate: '',
      form: {
        transaction: '',
        return_date: new Date().toISOString().split('T')[0],
        rent_fee: '',
      },
      message: '',
      error: false,
    }
  },
  computed: {
    uniqueBooks() {
      const seen = new Map()
      for (const txn of this.activeTransactions) {
        if (!seen.has(txn.book_id)) {
          seen.set(txn.book_id, {
            book_id: txn.book_id,
            book_title: txn.book_title,
          })
        }
      }
      return Array.from(seen.values())
    },
    filteredMembers() {
      const filtered = this.activeTransactions
        .filter((txn) => txn.book_id === this.selectedBookId)
        .map((txn) => ({
          member_id: txn.member_id,
          member_name: txn.member_name,
        }))

      // Remove duplicates
      return filtered.filter((v, i, a) => a.findIndex((t) => t.member_id === v.member_id) === i)
    },
  },
  async created() {
    try {
      const res = await axios.get('http://localhost:8000/api/transactions/')
      this.activeTransactions = res.data.filter((txn) => txn.return_date === null)
    } catch (err) {
      this.error = true
      this.message = '❌ Failed to load transactions.'
    }
  },
  methods: {
    updateMemberList() {
      this.selectedMemberId = ''
      this.issueDate = ''
      this.form.transaction = ''
    },
    updateIssueDate() {
      const txn = this.activeTransactions.find(
        (t) => t.book_id === this.selectedBookId && t.member_id === this.selectedMemberId,
      )
      if (txn) {
        this.issueDate = txn.issue_date
        this.form.transaction = txn.id
      } else {
        this.issueDate = ''
        this.form.transaction = ''
      }
    },
    async returnBook() {
      if (!this.form.transaction) {
        this.error = true
        this.message = '❌ Please select a valid book and member combination.'
        return
      }

      this.message = ''
      this.error = false

      try {
        const payload = {
          return_date: this.form.return_date,
          rent_fee: parseFloat(this.form.rent_fee),
        }
        await axios.post(
          `http://localhost:8000/api/transactions/${this.form.transaction}/return/`,
          payload,
        )
        this.message = '✅ Book returned successfully!'

        this.selectedBookId = ''
        this.selectedMemberId = ''
        this.issueDate = ''
        this.form = {
          transaction: '',
          return_date: new Date().toISOString().split('T')[0],
          rent_fee: '',
        }

        setTimeout(() => this.$router.push('/transactions'), 1000)
      } catch (err) {
        this.error = true
        this.message = err.response?.data?.error || '❌ Failed to return book.'
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

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

select,
input[type='date'],
input[type='number'] {
  width: 100%;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  background-color: #fff;
}

input[readonly] {
  background-color: #f5f5f5;
}

button {
  width: 100%;
  padding: 10px;
  border-radius: 6px;
  background-color: #ff9800;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #fb8c00;
}

.back-button {
  background-color: #666;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  margin-bottom: 20px;
  width: auto;
}

.back-button:hover {
  background-color: #555;
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
