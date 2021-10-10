<template>
  <div class="pages_dashboard__wrapper">
    <div class="head">Statistics</div>
    <div class="box__wrapper">

      <div class="box">
        <div class="box-head">Users</div>
        <div class="box-content">{{ users.length }}</div>
      </div>

      <div class="box">
        <div class="box-head">Makers</div>
        <div class="box-content">{{ info.makers.length }}</div>
      </div>

      <div class="box">
        <div class="box-head">Types</div>
        <div class="box-content">{{ info.types.length }}</div>
      </div>

      <div class="box">
        <div class="box-head">Elements</div>
        <div class="box-content">{{ info.elements.length }}</div>
      </div>

      <div class="box">
        <div class="box-head">Modifications</div>
        <div class="box-content">{{ info.modifications.length }}</div>
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
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
    this.getUsers();
  },
  computed: {
    info() {
      return this.$store.getters.getInfo;
    },
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
  },
};
</script>

<style lang="scss">
  .pages_dashboard__wrapper {
    .head {
      margin-bottom: 50px;
      font-weight: bold;
      font-size: 1.5em;
    }
    .box__wrapper {
      display: flex;
      flex-wrap: wrap;
      .box {
        margin: 10px;
        padding: 20px;
        background: #1e1e1e;
        border-radius: 10px;
        box-shadow: inset 0px 0px 8px #0606062d;
        .box-head {
          text-align: center;
          font-weight: 600;
        }
        .box-content {
          text-align: center;
          margin-top: 5px;
          color: #767676;
        }
      }
    }
  }
</style>
