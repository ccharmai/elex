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
      const startTime = new Date();
      const localToken = localStorage.getItem('token');
      if (!localToken) {
        this.endLoading(new Date() - startTime, '/auth');
        return;
      }
      const loginUrl = `${this.$store.getters.api}/token.info/`;
      axios.post(loginUrl, { token: localToken })
        .then((res) => {
          if (res.data.status === 'ok') {
            this.$store.dispatch('setUser', { ...res.data });
            this.endLoading(new Date() - startTime);
          } else {
            localStorage.removeItem('token');
            this.endLoading(new Date() - startTime, '/auth');
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    endLoading(time, url = null) {
      if (time / 1000 >= 1) this.$store.dispatch('setPreloader', false);
      else {
        setTimeout(() => {
          this.$store.dispatch('setPreloader', false);
          if (url) this.$router.push(url);
        }, (1.5 - time / 1000) * 1000);
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
