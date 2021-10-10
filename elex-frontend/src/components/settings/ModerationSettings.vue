<template>
  <div class="setings_moderation_settings__wrapper">
    <div class="settings-title">Модерация записей</div>
  </div>
</template>

<script>
export default {
  created() {
    if (!this.$store.getters.getUser.admin) this.$router.push('/');
  },
};
</script>

<style lang="scss">
  //.setings_moderation_settings__wrapper {}
</style>
