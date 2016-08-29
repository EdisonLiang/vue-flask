<template>
<h4>{{article.heading}}</h4>
<hr/>
<p>{{article.text}}</p>
<round-image v-for="image in article.images"></round-image>
</template>

<script>
import RoundImage from './RoundImage'
export default {
  props: ['article'],
  components: {
    RoundImage
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
</style>
