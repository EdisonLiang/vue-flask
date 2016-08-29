<template>
  <h3>Home</h3>
  <home-article v-for="article in articles" :article="article"></home-article>
</template>
<script>
// import Vue from 'vue'
import HomeArticle from './HomeArticle'
import state from '../App'
export default {
  components: {
    HomeArticle
  },
  ready () {
    this.getHome()
  },
  data () {
    return {
      articles: state.home
    }
  },
  methods: {
    getHome: function () {
      this.$http.get('/api/home').then((response) => {
        console.log(response.json())
        state.home = JSON.parse(response.data)
        console.log('called', this)
      }, (response) => {
        console.log('network error')
      })
    }
  },
  events: {
    'home-updated': function () {
      console.log('event')
    }
  }
}

</script>

<style>

</style>
