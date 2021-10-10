<template>
  <div class="page_modifications__wrapper">
    <div class="page-head">Modifications</div>
    <div class="loader" v-if="info.loading"><Loader /></div>
    <div class="table-content" v-if="!info.loading">
      <Table :info="displayElements" :add="true">
        <div class="add">
          <div class="h">Добавить модификацию</div>
          <div class="form">
            <div class="row">
              <div class="label">Предмет</div>
              <select v-model="addItemId">
                <option disabled selected :value="null">Выберите предмет</option>
                <option
                  v-for="el in info.elements"
                  :key="el.id"
                  :value="el.id"
                >{{ info.types.find(t => t.id === el.type).name }} {{ el.name }}</option>
              </select>
            </div>
            <div class="row">
              <div class="label">Name</div>
              <input type="text" v-model="addName">
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
      addItemId: null,
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
      return this.info.modifications.map((modification) => ({
        item: this.info.elements.find((item) => item.id === modification.item).name,
        name: modification.name,
      }));
    },
    canAdd() {
      if (!this.addName || !this.addItemId) return false;
      return true;
    },
  },
  methods: {
    add() {
      if (!this.canAdd) return;
      const url = `${this.$store.getters.api}/add.modification/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, { token, name: this.addName, item: this.addItemId })
        .then((res) => {
          if (res.data.status === 'ok') {
            if (res.data.obj) this.$store.dispatch('addItem', { field: 'modifications', obj: res.data.obj });
            else this.toast('На модерации');
            this.addName = '';
            this.addItemId = null;
          }
        });
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
