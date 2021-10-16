<template>
  <div class="setings_moderation_settings__wrapper">
    <div class="settings-title">Модерация записей</div>

    <ModerationList name="Properties" />
    <ModerationList name="Makers" />
    <ModerationList name="Types" />
    <ModerationList name="Elements" />
    <ModerationList name="Modifications" />

  </div>
</template>

<script>
import ModerationList from '@/components/settings/lib/ModerationList.vue';

export default {
  components: {
    ModerationList,
  },
  created() {
    if (!this.$store.getters.getUser.admin) this.$router.push('/');
  },
};
</script>

<style lang="scss">
  .setings_moderation_settings__wrapper {
    overflow: scroll;
    max-height: calc(100% + 20px);
  }
</style>
