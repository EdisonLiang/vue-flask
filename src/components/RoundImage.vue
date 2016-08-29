<template>
    <div class="roundimage" v-bind:style="{ backgroundImage: 'url(' + image + ')' }">
      <span v-on:click="displayUploadForm" class="glyphicon glyphicon-plus" aria-hidden="true"></span>
      <style v-if="image" lang="css">
      .roundimage span {
        display: none;
      }
      </style>
    </div>
    <upload-form></upload-form>
</template>

<script>
import UploadForm from './UploadForm'
export default {
  components: {
    UploadForm
  },
  data () {
    return {
      image: '',
      showUpload: true
    }
  },
  methods: {
    displayUploadForm: function (event) {
      this.$broadcast('show-upload')
    }
  }
}
</script>

<style lang="sass">
@import '../sass/variables.sass'

.roundimage
  width: 120px
  height: 120px
  color: $body-bg
  background-color: $brand-primary
  border-radius: 50%
  text-align: center
  font-size: 20px
  background-size: contain

  span
    line-height: 120px

</style>
