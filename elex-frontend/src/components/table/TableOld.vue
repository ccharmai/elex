<template>
  <div class="table_table__wrapper">
    <table v-if="info.length > 0">
      <tr class="table_head"><th v-for="i in header" :key="i">{{ i }}</th></tr>
      <tr class="table_row" v-for="i in info" :key="i.id">
        <td v-for="k in header" :key="`${i.id}${k}`">{{ i[k] }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    info: { type: Array },

    // defaul not show id in table
    showId: { type: Boolean, default: false },

    // add bottom field
    add: { type: Boolean, default: false },
  },
  computed: {
    header() {
      if (!this.info && this.info.length === 0) return [];
      let keys = Object.keys(this.info[0]);
      if (!this.showId) keys = keys.filter((k) => k !== 'id');
      return keys;
    },
  },
};
</script>

<style lang="scss">
  .table_table__wrapper {
    table {
      width: 100%;
      text-align: center;
      border-collapse: collapse;
    }
    td, th {
      padding: 10px;
      border-right: 2px solid #292929;
      &:last-child {
        border-right: none;
      }
      min-height: 20px;
    }
    tr {
      border-bottom: 2px solid #292929;
      &:last-child {
        border-bottom: none;
      }
    }
    .table_head {
      position: sticky;
      top: -20px;
      background-color: #1f1f1f;
      th {
        padding: 15px;
      }
      th:after {
        content: '';
        position: absolute;
        width: 100%;
        left: 0;
        right: 0;
        height: 2px;
        bottom: 0;
        background-color: #ff9633;
        box-shadow: 0px 3px 13px #ff963334;
      }
    }
    .table-input {
      width: 80%;
      outline: none;
      border: none;
      background: #2b2b2b;
      padding: 7px;
      font-size: 1em;
      border-radius: 10px;
      color: white;
      text-align: center;
    }
  }
</style>
