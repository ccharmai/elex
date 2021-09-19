<template>
  <div class="settings_users_settings__wrapper">
    <div class="settings-title">Настройки пользователей</div>
    <div class="table__wrapper">
      <table>
        <tr class="table-head">
          <th>ID</th>
          <th>Active</th>
          <th>Name</th>
          <th>Description</th>
          <th>Admin</th>
        </tr>
        <tr v-for="user in users" :key="user.id">
          <th>{{ user.id }}</th>
          <th class="pointer" @click="changeField(user.id, 'is_active', !user.is_active)">
            <div class="status" :class="{ 'false': !user.is_active }" />
          </th>
          <th>{{ user.name }}</th>
          <th>{{ user.description }}</th>
          <th class="pointer" @click="changeField(user.id, 'is_admin', !user.is_admin)">
            <div class="status" :class="{ 'false': !user.is_admin }" />
          </th>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    };
  },
  methods: {
    getUsers() {
      const url = `${this.$store.getters.api}/adm/get.users/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, { token })
        .then((res) => {
          if (res.data.status === 'ok') this.users = res.data.users;
          else { console.warn(res.data.msg); }
        })
        .catch((err) => { console.warn(err); });
    },
    changeField(user, field, value) {
      const url = `${this.$store.getters.api}/adm/set.user/`;
      const { token } = this.$store.getters.getUser;
      const settings = { token, user };
      settings[field] = value;
      axios.post(url, settings)
        .then((res) => {
          if (res.data.status === 'ok') {
            const userIndex = this.users.map((u) => u.id).indexOf(res.data.user.id);
            this.users.splice(userIndex, 1, res.data.user);
          }
        });
    },
  },
  created() {
    if (!this.$store.getters.getUser.admin) this.$router.push('/');
    this.getUsers();
  },
};
</script>

<style lang="scss">
  //.settings_users_settings__wrapper {}
</style>
