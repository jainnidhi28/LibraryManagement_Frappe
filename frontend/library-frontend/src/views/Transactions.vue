<template>
  <div class="transactions-dashboard">
    <h1>📘 Transactions Dashboard</h1>
    <router-link to="/transactions/issue" class="button">➕ Issue a Book</router-link>
    <router-link to="/transactions/return" class="button">🔁 Return a Book</router-link>
    <router-link to="/transactions" class="button">📋 View All Transactions</router-link>
  </div>
</template>

<script>
export default {
  name: 'Transactions',
}
</script>

<style scoped>
.transactions-dashboard {
  max-width: 600px;
  margin: 40px auto;
  text-align: center;
}
.button {
  display: inline-block;
  margin: 10px;
  padding: 10px 16px;
  background: #42a5f5;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-weight: bold;
}
.button:hover {
  background-color: #1e88e5;
}
</style>
