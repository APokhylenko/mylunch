<template>
  <div class="modal is-active">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head" style="text-align: center;">
      <p class="modal-card-title">
        <slot name="header"></slot>
      </p>
      <button class="delete" aria-label="close" @click="closeModalWindow"></button>
    </header>
    <section class="modal-card-body" style="text-align:center;">
      <slot></slot>
    </section>
    <footer class="modal-card-foot" style="justify-content: center;">
      <slot name="buttons"></slot>
    </footer>
  </div>
</div>
</template>
<script>
  import { eventBus } from '../main'
  export default {
    methods: {
      closeModalWindow() {
        eventBus.$emit('showModal', false)
      }
    }
  }
</script>