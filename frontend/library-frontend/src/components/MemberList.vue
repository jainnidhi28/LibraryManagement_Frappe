<template>
  <div class="member-list">
    <div class="header">
      <h2>📚 Members</h2>
      <router-link to="/add-member">
        <button class="add-member-btn">➕ Add New Member</button>
      </router-link>
    </div>

    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search members by name or email..."
      class="search-input"
    />

    <table class="members-table">
      <thead>
        <tr>
          <th @click="sortBy('name')">Name 🔽</th>
          <th @click="sortBy('email')">Email 🔽</th>
          <th @click="sortBy('outstanding_debt')">Outstanding Debt (₹) 🔽</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(member, index) in filteredAndSortedMembers"
          :key="member.id"
          :class="{ 'high-debt': member.outstanding_debt > 500 }"
          @click="showDebtWarning(member)"
        >
          <td>{{ member.name }}</td>
          <td>{{ member.email }}</td>
          <td>₹{{ Number(member.outstanding_debt).toFixed(2) }}</td>
          <td @click.stop>
            <router-link :to="`/edit-member/${member.id}`">
              <span class="edit-icon">✏️</span>
            </router-link>
            <span class="delete-icon" @click="deleteMember(member.id)">🗑️</span>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="modal-overlay" v-if="showModal">
      <div class="modal">
        <h3>⚠️ High Debt Alert</h3>
        <p>
          Member <strong>{{ selectedMember?.name }}</strong> has an outstanding debt of ₹{{
            selectedMember?.outstanding_debt
          }}.
        </p>
        <button @click="closeModal">Close</button>
      </div>
    </div>

    <div class="toast" v-if="toastMessage">{{ toastMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MemberList',
  data() {
    return {
      members: [],
      searchQuery: '',
      sortKey: '',
      sortAsc: true,
      toastMessage: '',
      showModal: false,
      selectedMember: null,
    }
  },
  computed: {
    filteredAndSortedMembers() {
      let result = this.members.filter((member) =>
        (member.name + member.email).toLowerCase().includes(this.searchQuery.toLowerCase()),
      )

      if (this.sortKey) {
        result.sort((a, b) => {
          let aVal = a[this.sortKey]
          let bVal = b[this.sortKey]

          if (typeof aVal === 'string') aVal = aVal.toLowerCase()
          if (typeof bVal === 'string') bVal = bVal.toLowerCase()

          return this.sortAsc ? (aVal > bVal ? 1 : -1) : aVal < bVal ? 1 : -1
        })
      }

      return result
    },
  },
  methods: {
    async fetchMembers() {
      try {
        const response = await axios.get('http://localhost:8000/api/members/')
        this.members = response.data
      } catch (error) {
        this.showToast('❌ Failed to fetch members')
        console.error(error)
      }
    },
    async deleteMember(id) {
      if (confirm('Are you sure you want to delete this member?')) {
        try {
          await axios.delete(`http://localhost:8000/api/members/${id}/`)
          this.members = this.members.filter((m) => m.id !== id)
          this.showToast('✅ Member deleted successfully')
        } catch (error) {
          this.showToast('❌ Failed to delete member')
          console.error(error)
        }
      }
    },
    showToast(message) {
      this.toastMessage = message
      setTimeout(() => {
        this.toastMessage = ''
      }, 3000)
    },
    sortBy(key) {
      if (this.sortKey === key) {
        this.sortAsc = !this.sortAsc
      } else {
        this.sortKey = key
        this.sortAsc = true
      }
    },
    showDebtWarning(member) {
      if (member.outstanding_debt > 500) {
        this.selectedMember = member
        this.showModal = true
      }
    },
    closeModal() {
      this.showModal = false
      this.selectedMember = null
    },
  },
  created() {
    this.fetchMembers()
  },
}
</script>

<style scoped>
.member-list {
  max-width: 1000px;
  margin: 30px auto;
  background: #fff;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.add-member-btn {
  background-color: #4a90e2;
  color: white;
  padding: 10px 16px;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
}

.add-member-btn:hover {
  background-color: #357ab8;
}

.search-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

.members-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 16px;
}

.members-table th,
.members-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
  cursor: pointer;
}

.members-table thead {
  background-color: #f4f4f4;
}

.members-table tr:hover {
  background-color: #f9f9f9;
}

.high-debt {
  background-color: #ffe5e5;
}

.edit-icon {
  cursor: pointer;
  margin-right: 10px;
  color: #3498db;
  font-size: 18px;
}

.delete-icon {
  cursor: pointer;
  color: #e74c3c;
  font-size: 18px;
}

.toast {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background: #2ecc71;
  color: white;
  padding: 12px 20px;
  border-radius: 6px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  font-weight: bold;
  z-index: 1000;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.modal {
  background: white;
  padding: 25px;
  border-radius: 10px;
  width: 350px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.modal h3 {
  margin-bottom: 10px;
  color: #e74c3c;
}

.modal button {
  margin-top: 15px;
  padding: 8px 16px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>
