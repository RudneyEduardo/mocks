<template>
  <div id="app">

      

      <Container></Container>


  </div>
</template>

<script>

  //
  //import Title from './components/Title'
  //import Cart from './components/Cart'
  //import Form from './components/Form'
  import Container from './components/Container'


 

  export default {
    name: 'App',
    components: {

      Container
       
     

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