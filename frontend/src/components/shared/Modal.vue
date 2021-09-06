<template>
  <div class="layou_modal__wrapper">
    <div class="close" @click="$emit('close')">
      <img src="../../assets/img/close.svg" alt="Close">
    </div>
    <div class="modal"><slot /></div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss">
  .layou_modal__wrapper {
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.6);
    .modal {
      background: #1F1F1F;
      padding: 20px;
      border-radius: 10px;
    }
    .close {
      position: fixed;
      top: 20px;
      right: 20px;
      cursor: pointer;
      img {
        width: 20px;
        height: 20px;
      }
    }
  }
</style>
