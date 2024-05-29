# App.vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">Create Recipe</router-link>
      <router-link to="/recipes">Recipe List</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  margin-bottom: 20px;
  background-color: #42b983;
  padding: 10px;
}

nav a {
  margin: 0 10px;
  text-decoration: none;
  color: white;
}

nav a.router-link-exact-active {
  font-weight: bold;
  color: yellow;
}
</style>
