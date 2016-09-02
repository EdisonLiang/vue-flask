<template>
  <h3>Home</h3>
  <home-article v-for="article in articles" :article="article" track-by="$index"></home-article>
</template>
<script>
// import Vue from 'vue'
import HomeArticle from './HomeArticle'
import { state } from '../App'
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
        var items = JSON.parse(response.data)
        // just assigning items to state.home doesn't trigger
        // UI update, therefore the use of splice and push
        // clear the array
        state.home.splice(0, state.home.length)
        items.forEach(function (val, index, items) {
          this.push(val)
        }, state.home)
      }, (response) => {
        console.log('network error')
      })
    }
  }
}

</script>

<style>

</style>
