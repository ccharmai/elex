<template>
  <div class="page_types__wrapper">
    <div class="page-head">Types</div>
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
      return this.info.types.map((type) => ({
        name: type.name,
        description: type.description,
      }));
    },
  },
};
</script>

<style lang="scss">
  .page_types__wrapper {
    .page-head {
      margin-bottom: 50px;
    }
  }
</style>
