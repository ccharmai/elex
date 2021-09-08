<template>
  <div class="page_elements__wrapper"></div>
</template>

<script>
export default {
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
};
</script>

<style lang="scss">
  //.page_elements__wrapper {}
</style>
