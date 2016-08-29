<template>
  <div id="store"></div>
</template>

<script>
var self = null
export default {
  ready () {
    self = this
    console.log('ready', self)
  },
  data () {
    return {
      state: {
        message: 'Hello!',
        home: [],
        dogs: [
          {'name': 'Winna'},
          {'name': 'Keyton'},
          {'name': 'Troy'},
          {'name': 'Star'},
          {'name': 'Rai'}
        ]
      }
    }
  },
  methods: {
    updateHome: function (event) {
      console.log('methods', this)
      this.$dispatch('home-updated')
    }
  },
  getHome: function () {
    console.log('old')
  }
}
</script>

<style scoped>
</style>
