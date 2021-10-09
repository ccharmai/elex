<template>
  <div class="page_elements__wrapper">
    <div class="page-head">Elements</div>
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
      return this.info.elements.map((element) => ({
        id: element.id,
        maker: this.info.makers.find((maker) => maker.id === element.maker).name,
        type: this.info.types.find((type) => type.id === element.type).name,
        name: element.name,
      }));
    },
  },
};
</script>

<style lang="scss">
  .page_elements__wrapper {
    .page-head {
      margin-bottom: 50px;
    }
  }
</style>
