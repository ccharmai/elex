<template>
  <div class="setings_logs_settings__wrapper">
    <div class="settings-title">Логи</div>
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="logs.length === 0" class="no-logs">Нет логов</div>
    <div v-else class="logs-list">
      <table>
        <tr class="list-header">
          <td>Model</td>
          <td>Author</td>
          <td>Comment</td>
          <td>Time</td>
        </tr>
        <tr v-for="log in logs" :key="log.id">
          <td>{{ log.model }}</td>
          <td>{{ log.author }}</td>
          <td>{{ log.comment }}</td>
          <td>{{ log.time }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  created() {
    if (!this.$store.getters.getUser.admin) this.$router.push('/');
    const url = `${this.$store.getters.api}/adm/get.logs/`;
    const { token } = this.$store.getters.getUser;
    this.loading = true;
    axios.post(url, { token })
      .then((res) => {
        if (res.data.status === 'ok') this.logs = res.data.logs;
      })
      .finally(() => {
        this.loading = false;
      });
  },
  data() {
    return {
      logs: [],
      loading: false,
    };
  },
};
</script>

<style lang="scss">
  .setings_logs_settings__wrapper {
    table {
      border-collapse: collapse;
      width: 100%;
      td {
        padding: 7px;
        text-align: center;
      }
      .list-header {
        td {
          border-bottom: 1px solid #ff9633;
        }
      }
    }
  }
</style>
