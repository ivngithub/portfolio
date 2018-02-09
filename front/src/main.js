import Vue from 'vue'
import App from './App.vue'
import Nav from './Nav.vue'


Vue.component('nav-left', Nav)

new Vue({
  el: '#app',
  render: h => h(App)
})
