<template>
  <div class="layout_page_preloader__wrapper">
    <div class="preloader">
        <loader
          object="#ff9633"
          color1="#ffffff"
          color2="#17fd3d"
          size="5"
          speed="2"
          bg="#343a40"
          objectbg="#999793"
          opacity="80"
          disableScrolling="true"
          name="box"
        />
    </div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss">
  .layout_page_preloader__wrapper {
    width: 100vw;
    height: 100vh;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #1F1F1F;
    display: flex;
    justify-content: center;
    align-items: center;
    .preloader {
      width: 100px;
      height: 100px;
    }
  }
</style>
