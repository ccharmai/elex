<template>
  <div class="page_makers__wrapper">
    <div class="page-head">Makers</div>
    <div class="loader" v-if="info.loading"><Loader /></div>
    <div class="table-content" v-if="!info.loading">
      <Table :info="displayElements" :add="true">
        <div class="add">
          <div class="h">Добавить производителя</div>
          <div class="form">
            <div class="row">
              <div class="label">Name</div>
              <input type="text" v-model="addName">
            </div>
            <div class="row">
              <div class="label">Description</div>
              <input type="text" v-model="addDescription">
            </div>
          </div>
          <div class="flex jcc">
            <div
              class="btn"
              :class="{ 'disabled': !canAdd }"
              @click="add"
            >Добавить</div>
          </div>
        </div>
      </Table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

import Loader from '@/components/shared/Loader.vue';
import Table from '@/components/table/Table.vue';

export default {
  components: {
    Loader,
    Table,
  },
  setup() {
    const toast = useToast();

    return {
      toast,
    };
  },
  data() {
    return {
      addName: '',
      addDescription: '',
    };
  },
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
  computed: {
    info() {
      return this.$store.getters.getInfo;
    },
    displayElements() {
      return this.info.makers.map((maker) => ({
        name: maker.name,
        description: maker.description,
      }));
    },
    canAdd() {
      if (!this.addName || !this.addDescription) return false;
      return true;
    },
  },
  methods: {
    add() {
      if (!this.canAdd) return;
      const url = `${this.$store.getters.api}/add.maker/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, { token, name: this.addName, description: this.addDescription })
        .then((res) => {
          if (res.data.status === 'ok') {
            if (res.data.obj) this.$store.dispatch('addItem', { field: 'makers', obj: res.data.obj });
            else this.toast('На модерации');
            this.addName = '';
            this.addDescription = '';
          }
        });
    },
  },
};
</script>

<style lang="scss">
  .page_makers__wrapper {
    .page-head {
      margin-bottom: 50px;
    }
  }
</style>
