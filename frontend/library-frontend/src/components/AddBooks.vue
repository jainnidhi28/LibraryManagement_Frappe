<template>
  <div class="add-book">
    <h2>Add New Book</h2>
    <form @submit.prevent="submitBook">
      <div>
        <label for="title">Title</label>
        <input v-model="book.title" id="title" required />
      </div>
      <div>
        <label for="authors">Authors</label>
        <input v-model="book.authors" id="authors" required />
      </div>
      <div>
        <label for="isbn">ISBN</label>
        <input v-model="book.isbn" id="isbn" required />
      </div>
      <div>
        <label for="publisher">Publisher</label>
        <input v-model="book.publisher" id="publisher" required />
      </div>
      <div>
        <label for="num_pages">Pages</label>
        <input type="number" v-model="book.num_pages" id="num_pages" required />
      </div>
      <div>
        <label for="stock">Stock</label>
        <input type="number" v-model="book.stock" id="stock" required />
      </div>
      <button type="submit">Add Book</button>
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
        num_pages: '',
        stock: '',
      },
    }
  },
  methods: {
    async submitBook() {
      try {
        await axios.post('http://localhost:8000/api/books/', this.book)
        this.$router.push('/books') // Redirect to the Book List page
      } catch (error) {
        console.error('Error adding book:', error)
      }
    },
  },
}
</script>

<style scoped>
.add-book {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 0 auto;
}

form div {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
}

button {
  background-color: #38a169;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  width: 100%;
}
</style>
