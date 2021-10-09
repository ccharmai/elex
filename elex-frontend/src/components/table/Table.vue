<template>
  <div class="table_table__wrapper">
    <div class="table">
      <div class="row head" :style="{ 'grid-template-columns': cssGridColumns }">
        <div v-for="headItem of head" :key="headItem">{{ headItem }}</div>
      </div>
      <div class="row" v-for="item in info" :key="item.id"
        :style="{ 'grid-template-columns': cssGridColumns }"
      >
        <div v-for="(value, key) of item" :key="item.id + key">
          {{ value }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    info: { type: Array },
  },
  computed: {
    head() {
      if (this.info.length === 0) return [];
      return Object.keys(this.info[0]);
    },
    cssGridColumns() {
      return `repeat(${this.head.length}, 1fr)`;
    },
  },
};
</script>

<style lang="scss">
  .table_table__wrapper {
    .row {
      display: grid;
    }
  }
</style>
