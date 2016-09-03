<template>
  <modal :show.sync="showModal" title="Choose file" :callback="submitDialog">
    <div slot="modal-header" class="modal-header">
      <h4 class="modal-title">Modal title</h4>
    </div>
    <div slot="modal-body" class="modal-body">Look at mah bodeeehh!!</div>
  </modal>
</template>

<script>
import { modal } from 'vue-strap'
export default {
  components: {
    modal
  },
  data () {
    return {
      showModal: false
    }
  },
  methods: {
    submitDialog: function (event) {
      console.log('dialog-complete')
      this.showModal = false
    }
  },
  events: {
    'show-upload': function () {
      this.showModal = true
      console.log('show-upload')
    }
  }
}
</script>

<style>

</style>
