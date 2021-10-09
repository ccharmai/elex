<template>
  <div class="page_modifications__wrapper">
    <div class="page-head">Modifications</div>
    <div class="loader" v-if="info.loading"><Loader /></div>
    <div class="table-content" v-if="!info.loading">
      <Table :info="displayElements" :add="true" />
    </div>
  </div>
</template>

<script>
import Loader from '@/components/shared/Loader.vue';
import Table from '@/components/table/Table.vue';

export default {
  components: {
    Loader,
    Table,
  },
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
  computed: {
    info() {
      return this.$store.getters.getInfo;
    },
    displayElements() {
      return this.info.modifications.map((modification) => ({
        id: modification.id,
        item: this.info.elements.find((item) => item.id === modification.item).name,
        name: modification.name,
      }));
    },
  },
};
</script>

<style lang="scss">
  .page_modifications__wrapper {
    .page-head {
      margin-bottom: 50px;
    }
  }
</style>
