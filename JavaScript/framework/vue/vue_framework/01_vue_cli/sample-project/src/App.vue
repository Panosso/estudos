<template>
  <div id="app">
    <p>{{ title }}</p>
  </div>
</template>

<script>

//Export a vue object, so this object can have watch, computed, data and more
export default {
  name: 'App',
  data(){
    return{
      title: "This is a title"
    }
  }
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
  background: chocolate;
}
</style>
