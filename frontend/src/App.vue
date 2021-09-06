<template>
  <div id="root">
    <div class="compose">
      <TheMenu class="layout-menu" />
      <div class="content">
        <router-view />
      </div>
    </div>
    <PagePreloader v-if="showPagePreloader" />
  </div>
</template>

<script>
import TheMenu from '@/components/layout/TheMenu.vue';
import PagePreloader from '@/components/layout/PagePreloader.vue';

export default {
  components: {
    TheMenu,
    PagePreloader,
  },
  computed: {
    showPagePreloader() {
      return this.$store.getters.showPagePreloader;
    },
  },
  created() {
    document.title = 'Elex';
    // some actions ...
    setTimeout(() => {
      this.$store.dispatch('setPreloader', false);
    }, 1000);
  },
};
</script>

<style lang="scss">
  #root {
    .compose {
      display: flex;
      width: 100%;
    }
    .content {
      width: 100%;
      min-height: 100%;
      padding: 20px;
    }
  }
</style>
