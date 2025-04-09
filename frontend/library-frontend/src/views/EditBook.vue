<template>
  <div class="edit-book">
    <h2>Edit Book</h2>
    <form @submit.prevent="updateBook">
      <label>Title</label>
      <input v-model="book.title" required />

      <label>Authors</label>
      <input v-model="book.authors" required />

      <label>ISBN</label>
      <input v-model="book.isbn" required />

      <label>Publisher</label>
      <input v-model="book.publisher" required />

      <label>Number of Pages</label>
      <input type="number" v-model="book.num_pages" required />

      <label>Stock</label>
      <input type="number" v-model="book.stock" required />

      <button type="submit">Update Book</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      book: {
        title: '',
        authors: '',
        isbn: '',
        publisher: '',
        num_pages: 0,
        stock: 0,
      },
    }
  },
  async mounted() {
    const bookId = this.$route.params.id
    try {
      const response = await axios.get(`http://localhost:8000/api/books/${bookId}/`)
      this.book = response.data
    } catch (err) {
      console.error('Failed to load book:', err)
    }
  },
  methods: {
    async updateBook() {
      const bookId = this.$route.params.id
      try {
        await axios.put(`http://localhost:8000/api/books/${bookId}/`, this.book)
        alert('Book updated successfully!')
        this.$router.push('/')
      } catch (err) {
        console.error('Update failed:', err)
        alert('Error updating book!')
      }
    },
  },
}
</script>

<style scoped>
.edit-book {
  max-width: 600px;
  margin: auto;
  padding: 24px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.edit-book h2 {
  text-align: center;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

input {
  padding: 10px;
  border: 1px solid #cbd5e0;
  border-radius: 6px;
}

button {
  background-color: #3182ce;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background-color: #2b6cb0;
}
</style>
