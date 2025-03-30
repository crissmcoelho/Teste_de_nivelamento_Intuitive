<template>
    <img alt="Vue logo" src="./assets/logo.png">
    <div><MyComponent /></div>
  </template>
  
  <script>
  import meu_componentes from './componentes/meu_omponentes.vue'
  
  export default {
    name: 'App',
    componentes: {
      meu_componentes
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
  }
  </style>