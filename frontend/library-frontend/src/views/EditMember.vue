<template>
  <div class="edit-member">
    <h2>Edit Member</h2>
    <form @submit.prevent="updateMember">
      <label>Name</label>
      <input v-model="member.name" required />

      <label>Email</label>
      <input v-model="member.email" required />

      <label>Outstanding Debt (₹)</label>
      <input type="number" v-model="member.outstanding_debt" required />

      <button type="submit">Update Member</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      member: {
        name: '',
        email: '',
        outstanding_debt: 0,
      },
    }
  },
  async mounted() {
    const id = this.$route.params.id
    try {
      const response = await axios.get(`http://localhost:8000/api/members/${id}/`)
      this.member = response.data
    } catch (err) {
      console.error('Failed to fetch member:', err)
    }
  },
  methods: {
    async updateMember() {
      const id = this.$route.params.id
      try {
        await axios.put(`http://localhost:8000/api/members/${id}/`, this.member)
        alert('Member updated successfully!')
        this.$router.push('/members')
      } catch (err) {
        console.error('Failed to update member:', err)
        alert('Error updating member.')
      }
    },
  },
}
</script>

<style scoped>
.edit-member {
  max-width: 600px;
  margin: auto;
  padding: 24px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.edit-member h2 {
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
