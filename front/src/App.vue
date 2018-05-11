<template>
  <div id="app">
    <nav-left></nav-left>
    <main>
      <div class="row">
        <div class="col s12 m4">
          <h2 class="right-align hide-on-small-only">{{ message }}</h2>
          <h2 class="center-align hide-on-med-and-up">{{ message }}</h2>
        </div>
      </div>
      <div class="row">
        <div class="col s12 m4">
          <h4 class="right-align hide-on-small-only">mail:</h4>
          <h4 class="center-align hide-on-med-and-up">mail:</h4>
        </div>
        <div class="col s12 m8">
          <h4 class="left-align hide-on-small-only">{{ mail }}</h4>
          <h4 class="center-align hide-on-med-and-up">{{ mail }}</h4>
        </div>
      </div>
      <div class="row">
        <div class="col s12 m4">
          <h4 class="right-align hide-on-small-only">skype:</h4>
          <h4 class="center-align hide-on-med-and-up">skype:</h4>
        </div>
        <div class="col s12 m8">
          <h4 class="left-align hide-on-small-only">{{ skype }}</h4>
          <h4 class="center-align hide-on-med-and-up">{{ skype }}</h4>
        </div>
      </div>
      <div class="row">
        <div class="col s12 m4">
          <h4 class="right-align hide-on-small-only">git:</h4>
          <h4 class="center-align hide-on-med-and-up">git:</h4>
        </div>
        <div class="col s12 m8">
          <h4 class="left-align hide-on-small-only">{{ git }}</h4>
          <h4 class="center-align hide-on-med-and-up">{{ git }}</h4>
        </div>
      </div>
      <div class="row">
        <div class="col s12 m4">
          <h4 class="right-align hide-on-small-only">docker:</h4>
          <h4 class="center-align hide-on-med-and-up">docker:</h4>
        </div>
        <div class="col s12 m8">
          <h4 class="left-align hide-on-small-only">{{ docker }}</h4>
          <h4 class="center-align hide-on-med-and-up">{{ docker }}</h4>
        </div>
      </div>
    </main>
    <footer>

    </footer>
  </div>
</template>

<script>
export default {
  el: '#app',
  data () {
    return {message: 'portfolio:'.toUpperCase(),
            mail: 'ivn@li.ru',
            skype: 'ivnminin',
            git: 'github.com/ivngithub',
            docker: 'hub.docker.com/u/ivndocker/'
    }
  }
}
</script>

<style>
  main, footer {
    padding-left: 300px;
  }
  h2 {
    font-weight: 600;
    text-align: center;
  }
  h5 {
    font-weight: 200;
  }
  @media only screen and (max-width : 992px) {
    main, footer {
      padding-left: 0;
    }
  }
</style>
