<template>
  <div class="book-list">
    <div class="search-import">
      <input
        v-model="searchQuery"
        @input="searchBooks"
        placeholder="🔍 Search by title or author..."
      />
      <div class="action-buttons">
        <router-link to="/add-book">
          <button>Add New Book</button>
        </router-link>
        <router-link to="/import-books">
          <button>Import Books</button>
        </router-link>
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Authors</th>
          <th>ISBN</th>
          <th>Publisher</th>
          <th>Pages</th>
          <th>Stock</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.title }}</td>
          <td>{{ book.authors }}</td>
          <td>{{ book.isbn }}</td>
          <td>{{ book.publisher }}</td>
          <td>{{ book.num_pages }}</td>
          <td>{{ book.stock }}</td>
          <td>
            <router-link :to="`/edit-book/${book.id}`">
              <span class="edit-icon">✏️</span>
            </router-link>
            <span class="delete-icon" @click="deleteBook(book.id)">🗑️</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      books: [],
      searchQuery: '',
    }
  },
  mounted() {
    this.fetchBooks()
  },
  methods: {
    async fetchBooks() {
      const response = await axios.get('http://localhost:8000/api/books/')
      this.books = response.data
    },
    async searchBooks() {
      if (this.searchQuery.trim() === '') {
        this.fetchBooks()
        return
      }
      try {
        const response = await axios.get(
          `http://localhost:8000/api/books/search/?query=${this.searchQuery}`,
        )
        this.books = response.data
      } catch (error) {
        console.error('Search error:', error)
      }
    },
    async deleteBook(id) {
      if (confirm('Are you sure you want to delete this book?')) {
        try {
          await axios.delete(`http://localhost:8000/api/books/${id}/`)
          this.books = this.books.filter((book) => book.id !== id)
        } catch (error) {
          console.error('Error deleting book:', error)
        }
      }
    },
  },
}
</script>

<style scoped>
.book-list {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.search-import {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.search-import input {
  flex: 1;
  padding: 10px;
  font-size: 1rem;
  margin-right: 20px;
  border-radius: 6px;
  border: 1px solid #e2e8f0;
  min-width: 250px;
}

.action-buttons {
  display: flex;
  gap: 10px;
}

button {
  background-color: #38a169;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background-color: #2f855a;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

thead {
  background-color: #edf2f7;
}

th,
td {
  padding: 10px;
  border: 1px solid #e2e8f0;
  text-align: left;
}

.edit-icon {
  cursor: pointer;
  margin-right: 8px;
  color: #3498db;
  font-size: 18px;
}

.delete-icon {
  cursor: pointer;
  color: #e74c3c;
  font-size: 18px;
}
</style>
