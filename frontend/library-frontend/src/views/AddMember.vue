<template>
  <div class="add-member">
    <h2>➕ Add Member</h2>
    <form @submit.prevent="submitMember" class="add-form">
      <input v-model="form.name" type="text" placeholder="Name" required />
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input
        v-model="form.outstanding_debt"
        type="number"
        step="0.01"
        placeholder="Outstanding Debt"
        required
      />
      <button type="submit">Add Member</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AddMember',
  data() {
    return {
      form: {
        name: '',
        email: '',
        outstanding_debt: '',
      },
    }
  },
  methods: {
    async submitMember() {
      try {
        await axios.post('http://localhost:8000/api/members/', this.form)
        this.$router.push('/members')
      } catch (error) {
        console.error('Failed to add member:', error)
      }
    },
  },
}
</script>

<style scoped>
.add-member {
  max-width: 500px;
  margin: 40px auto;
  background: #f9f9f9;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.add-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.add-form input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
}

.add-form button {
  background-color: #38a169;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.add-form button:hover {
  background-color: #2f855a;
}
</style>
