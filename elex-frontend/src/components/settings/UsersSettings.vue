<template>
  <div class="settings_users_settings__wrapper">
    <div class="settings-title">Настройки пользователей</div>
    <div class="users__wrapper">
      <div class="row head">
        <div>id</div>
        <div>Active</div>
        <div>Name</div>
        <div>Description</div>
        <div>Admin</div>
        <div>Delete</div>
      </div>
      <div class="row" v-for="user in users" :key="user.id"
        :class="{ 'current': user.name === userName }"
      >
        <div>{{ user.id }}</div>
        <div>
          <div class="indicator" :class="{ 'active': user.is_active }"
            @click="changeField(user.id, 'is_active', !user.is_active)">
          </div>
        </div>
        <div>{{ user.name }}</div>
        <div>{{ user.description?.length > 0 ? user.description : '-' }}</div>
        <div>
          <div class="indicator" :class="{ 'active': user.is_admin }"
            @click="changeField(user.id, 'is_admin', !user.is_admin)">
          </div>
        </div>
        <div class="delete"
          @click="deleteUser(user.id, user.name)">
          {{ user.name === userName ? '' : '𐄂' }}</div>
      </div>
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
    deleteUser(userId, name) {
      if (name === this.userName) return;
      const url = `${this.$store.getters.api}/adm/del.user/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, { token, user: userId })
        .then((res) => {
          if (res.data.status === 'ok') this.users = this.users.filter((u) => u.id !== userId);
        });
    },
  },
  created() {
    if (!this.$store.getters.getUser.admin) this.$router.push('/');
    this.getUsers();
  },
  computed: {
    userName() {
      return this.$store.getters.getUser.name;
    },
  },
};
</script>

<style lang="scss">
  .settings_users_settings__wrapper {
    .users__wrapper {
      overflow: scroll;
      max-height: calc(100vh - 100px);
      margin-top: 50px;
      .row {
        padding: 10px;
        display: grid;
        align-items: center;
        grid-template-columns: 1fr 1fr 2fr 3fr 1fr 1fr;
        & > div {
          text-align: center;
        }
        &.head {
          position: sticky;
          top: 0;
          background: #1f1f1f;
          border-bottom: 1px solid #ff9633;
          margin-bottom: 10px;
          & > div {
            padding-bottom: 20px;
          }
        }
        &.current {
          opacity: 0.5;
        }
      }
      .indicator {
        height: 10px;
        width: 10px;
        background: #580000;
        margin: 0 auto;
        border-radius: 9999px;
        cursor: pointer;
        &.active {
          background: #005200;
        }
      }
      .delete {
        cursor: pointer;
        color: #a50000;
        font-weight: bold;
      }
    }
  }
</style>
