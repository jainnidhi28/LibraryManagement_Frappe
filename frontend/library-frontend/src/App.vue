<template>
  <div id="app">
    <header>
      <h1>📚 Library Management</h1>
      <nav>
        <router-link to="/">🏠 Home</router-link>
        <router-link to="/books">📖 Books</router-link>
        <router-link to="/members">👥 Members</router-link>
        <router-link to="/transactions">🔁 Transactions</router-link>
      </nav>
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
body {
  font-family: 'Segoe UI', sans-serif;
  margin: 0;
  background: #f8f9fa;
}
#app {
  text-align: center;
}
header {
  background-color: #0077cc;
  color: white;
  padding: 20px;
}
nav {
  margin-top: 10px;
}
nav a {
  color: white;
  margin: 0 15px;
  text-decoration: none;
  font-weight: bold;
}
nav a:hover {
  text-decoration: underline;
}
main {
  padding: 30px;
}
</style>
