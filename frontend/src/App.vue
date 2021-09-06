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
import axios from 'axios';
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
    this.auth();
  },
  methods: {
    auth() {
      const startTime = performance.now();
      const localToken = localStorage.getItem('token');
      if (!localToken) {
        this.endLoading(performance.now() - startTime);
        return;
      }
      const loginUrl = `${this.$store.getters.api}/token.info/`;
      axios.post(loginUrl, { token: localToken })
        .then((res) => {
          console.log(res.data);
          this.endLoading(performance.now() - startTime);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    endLoading(time) {
      if (time >= 1) this.$store.dispatch('setPreloader', false);
      else {
        setTimeout(() => {
          this.$store.dispatch('setPreloader', false);
        }, (1.5 - time) * 1000);
      }
    },
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
