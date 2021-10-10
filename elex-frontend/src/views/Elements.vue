<template>
  <div class="page_elements__wrapper">
    <div class="page-head">Elements</div>
    <div class="loader" v-if="info.loading"><Loader /></div>
    <div class="table-content" v-if="!info.loading">
      <Table :info="displayElements" :add="true">
        <div class="add">
          <div class="h">Добавить элемент</div>
          <div class="form">
            <div class="row">
              <div class="label">Производитель</div>
              <select v-model="addMakerId">
                <option disabled selected :value="null">Выберите производителя</option>
                <option
                  v-for="el in info.makers"
                  :key="el.id"
                  :value="el.id"
                >{{ el.name }}</option>
              </select>
            </div>
            <div class="row">
              <div class="label">Тип</div>
              <select v-model="addTypeId">
                <option disabled selected :value="null">Выберите тип</option>
                <option
                  v-for="el in info.types"
                  :key="el.id"
                  :value="el.id"
                >{{ el.name }}</option>
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
      addTypeId: null,
      addMakerId: null,
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
      return this.info.elements.map((element) => ({
        maker: this.info.makers.find((maker) => maker.id === element.maker).name,
        type: this.info.types.find((type) => type.id === element.type).name,
        name: element.name,
      }));
    },
    canAdd() {
      if (!this.addName || !this.addTypeId || !this.addMakerId) return false;
      return true;
    },
  },
  methods: {
    add() {
      if (!this.canAdd) return;
      const url = `${this.$store.getters.api}/add.element/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, {
        token, name: this.addName, type: this.addTypeId, maker: this.addMakerId,
      })
        .then((res) => {
          if (res.data.status === 'ok') {
            console.log(res.data);
            if (res.data.obj) this.$store.dispatch('addItem', { field: 'elements', obj: res.data.obj });
            else this.toast('На модерации');
            this.addName = '';
            this.addTypeId = null;
            this.addMakerId = null;
          }
        });
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
