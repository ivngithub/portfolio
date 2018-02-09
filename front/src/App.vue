<template>
  <div id="app">
    <nav-left></nav-left>
    <main>
      <h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2><h2>{{ message }}</h2>
    </main>
    <footer>

    </footer>
  </div>
</template>

<script>
export default {
  el: '#app',
  data () {
    return {message: 'Привет, Vue!',
            footer: 'Footer Content'
    }
  }
}
</script>

<style>
  main, footer {
    padding-left: 300px;
  }

  @media only screen and (max-width : 992px) {
    main, footer {
      padding-left: 0;
    }
  }
</style>
