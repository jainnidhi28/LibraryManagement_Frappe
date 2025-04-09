<template>
  <div class="import-books">
    <h2>Import Books</h2>
    <form @submit.prevent="importBooks">
      <div>
        <label for="title">Keyword (optional)</label>
        <input v-model="title" id="title" />
      </div>
      <div>
        <label for="count">Number of Books</label>
        <input type="number" v-model="count" id="count" required />
      </div>
      <button type="submit">Import Books</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      title: '',
      count: 20, // Default to 20 books
    }
  },
  methods: {
    async importBooks() {
      try {
        await axios.post('http://localhost:8000/api/books/import_books/', {
          title: this.title,
          count: this.count,
        })
        this.$router.push('/books') // Redirect to Book List page after importing
      } catch (error) {
        console.error('Error importing books:', error)
      }
    },
  },
}
</script>

<style scoped>
.import-books {
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
