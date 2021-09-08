<template>
  <div class="views_page_not_found__wrapper">
    <div class="box">
      <div class="big">404</div>
      <div class="mini">Страница не найдена</div>
    </div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss">
  .views_page_not_found__wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    text-align: center;
    .big {
      font-weight: bold;
      font-size: 5em;
    }
    .mini {
      font-size: 1.5em;
    }
  }
</style>
