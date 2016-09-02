<template>
<div>
  <navbar>
    <a href="/" title="Home" slot="brand" class="navbar-brand">Kungsängsliljan</a>
    <li><a v-link="{ path: '/home' }" data-toggle="collapse" data-target="#navbar">Home</a></li>
    <li><a v-link="{ path: '/about' }" data-toggle="collapse" data-target="#navbar">About</a></li>
    <li><a v-link="{ path: '/dogs' }" data-toggle="collapse" data-target="#navbar">Dogs</a></li>
    <dropdown text="dropdown"></dropdown>
  </navbar>
  <div class="container">
    <div class="main">
      <!-- main view -->
      <router-view>
      </router-view>
    </div>
  </div>

</div>
</template>

<script>
import { navbar, dropdown } from 'vue-strap'

var state = {
  home: [ ],
  dogs: [ ]
}

export default {
  state,
  components: {
    navbar,
    dropdown
  },
  data () {
    return {
    }
  }
}

</script>

<style lang="sass">
@import 'sass/variables.sass'
@import '../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap'

.main
  margin-top: 60px
  height: calc(100vh - 100px)

</style>
