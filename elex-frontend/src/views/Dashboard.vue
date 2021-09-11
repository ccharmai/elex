<template>
  <div class="pages_dashboard__wrapper"></div>
</template>

<script>
export default {
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
};
</script>

<style lang="scss">
  //.pages_dashboard__wrapper {}
</style>
