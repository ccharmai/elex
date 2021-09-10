<template>
  <div class="layouts_mini_menu__wrapper">
    <div class="el" @click="$router.push('/settings'); $emit('close')">Настройки акаунта</div>
    <div class="el" @click="logout()">Выйти из аккаунта</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    logout() {
      const token = window.localStorage.getItem('token');
      const deleteUrl = `${this.$store.getters.api}/token.delete/`;
      axios.post(deleteUrl, { token })
        .then((res) => {
          if (res.data.status === 'ok') {
            window.localStorage.removeItem('token');
            this.$store.dispatch('setUser', null);
            this.$router.push('/auth');
          }
        });
    },
  },
};
</script>

<style lang="scss">
  .layouts_mini_menu__wrapper {
    min-height: 50px;
    background: #1F1F1F;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 10px;
    .el {
      width: 100%;
      text-align: center;
      color: #7d7a7a;
      padding: 5px;
      cursor: pointer;
      border-bottom: 2px solid #333333;
      &:last-child {
        border-bottom: none;
      }
    }
  }
</style>
