<template>
  <div class="page_library__wrapper">
    <div class="page-head">Library</div>
    <div class="table">
      <div class="row head">
        <div>Элемент</div>
        <div>Производитель</div>
        <div>Модификация</div>
        <div>Свойство</div>
      </div>
      <div class="row" v-for="element in info.elements" :key="element.id">
        <div class="flex aic jcc">
          <div>{{ element.name }}</div>
        </div>
        <div class="flex aic jcc">
          <div>{{ info.makers.find(m => m.id === element.maker).name }}</div>
        </div>
        <div class="special-row"
          :style="`grid-template-rows:
            repeat(${getItemModifications(element.id).length}, 1fr);`"
        >
          <div
            class="flex aic jcc"
            v-for="modification in getItemModifications(element.id)"
            :key="modification.id"
          >
            <div>{{ modification.name }}</div>
          </div>
        </div>
        <div class="special-row"
          :style="`grid-template-rows:
            repeat(${getItemModifications(element.id).length}, 1fr);`"
        >
          <div v-for="modification in getItemModifications(element.id)" :key="modification.id" >
            <div v-for="prop in getModificationsProperties(modification.id)" :key="prop.id"
              class="prop"
            >
              {{ prop.name }} {{ prop.value }} {{ prop.dimension }}
            </div>
            <div class="add-btn" @click="addElId = modification.id, showAdd = true">Добавить</div>
          </div>
        </div>
      </div>
    </div>
    <Modal v-if="showAdd" @close="showAdd = false">
      <div class="modal">
        <div class="h">Добавить свойство</div>
        <div v-if="addElId !== -1">
          <div>Модификация - <i>{{ info.modifications.find(m => m.id === addElId).name }}</i></div>
          <div class="form">
            <Input placeholder="Свойство" v-model="addName" />
            <Input placeholder="Значение" v-model="addValue" />
            <Input placeholder="Размерность" v-model="addDimension" />
          </div>
          <div class="template">
            <div value="null">Использовать шаблон</div>
            <select v-model="templateId">
              <option selected>Шаблон не выбран</option>
              <option
                v-for="(option, index) in template"
                :key="option.field + option.dimension"
                :value="index"
              >
                {{ option.field }} ({{ option.dimension }}.)
              </option>
            </select>
          </div>
          <div class="flex jcc">
            <div
              class="add-btn"
              :class="{ 'disabled': !canAdd }"
              @click="add"
            >Добавить</div>
          </div>
        </div>
      </div>
    </Modal>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

import Modal from '@/components/shared/Modal.vue';
import Input from '@/components/shared/Input.vue';

export default {
  components: {
    Modal,
    Input,
  },
  setup() {
    const toast = useToast();

    return {
      toast,
    };
  },
  data() {
    return {
      templateId: null,
      showAdd: false,
      addElId: -1,
      addName: '',
      addValue: null,
      addDimension: '',
      template: [
        { field: 'Вес', dimension: 'гр' },
        { field: 'Вес', dimension: 'кг' },
        { field: 'Длина', dimension: 'м' },
        { field: 'Ширина', dimension: 'м' },
        { field: 'Высота', dimension: 'м' },
      ],
    };
  },
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
  computed: {
    info() {
      return this.$store.getters.getInfo;
    },
    canAdd() {
      if (!this.addName || !this.addValue || !this.addDimension) return false;
      return true;
    },
  },
  methods: {
    getItemModifications(itemId) {
      return this.info.modifications.filter((m) => m.item === itemId);
    },
    getModificationsProperties(modId) {
      return this.info.properties.filter((p) => p.modification === modId);
    },
    selectTemplate(value) {
      console.log(value);
    },
    onNameOrDimensionsChange() {
      let counter = 0;
      const template = this.template.find((t) => {
        if (t.field.toLowerCase() === this.addName.toLowerCase()
        && t.dimension.toLowerCase() === this.addDimension.toLowerCase()) {
          return true;
        }
        counter += 1;
        return false;
      });
      if (template) this.templateId = counter;
      else this.templateId = null;
    },
    add() {
      if (!this.canAdd) return;
      const url = `${this.$store.getters.api}/add.property/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, {
        token,
        modification: this.addElId,
        name: this.addName,
        value: this.addValue,
        dimension: this.addDimension,
      })
        .then((res) => {
          if (res.data.status === 'ok') {
            if (res.data.obj) this.$store.dispatch('addItem', { field: 'properties', obj: res.data.obj });
            else this.toast('На модерации');

            this.addName = '';
            this.addValue = '';
            this.addDimension = '';
          }
        });
    },
  },
  watch: {
    templateId() {
      if (this.templateId === 'Шаблон не выбран') {
        this.addName = '';
        this.addDimension = '';
      } else if (this.templateId !== null) {
        const template = this.template[this.templateId];
        this.addName = template.field;
        this.addDimension = template.dimension;
      }
    },
    addName() {
      this.onNameOrDimensionsChange();
    },
    addDimension() {
      this.onNameOrDimensionsChange();
    },
  },
};
</script>

<style lang="scss">
  .page_library__wrapper {
    .page-head {
      margin-bottom: 50px;
    }
    .table {
      .row {
        display: grid;
        grid-template-columns: 1fr 2fr 2fr 3fr;
        border-bottom: 1px solid #2c2c2c;
        &:nth-child(odd) {
          background: #1c1c1c;
        }
        &:last-child {
          border-bottom: none;
        }
        & > div {
          padding: 10px;
          text-align: center;
          border-right: 1px solid #2c2c2c;
          &:last-child {
            border-right: none;
          }
        }
        &.head {
          position: sticky;
          top: 0;
          background: #1f1f1f;
          border-bottom: 1px solid #ff9633;
          & > div {
            padding-bottom: 20px;
          }
        }
        .special-row {
          display: grid;
          & > div {
            padding: 7px;
            border-bottom: 3px solid #222222;
            &:last-child {
              border-bottom: none;
            }
          }
          .prop {
            font-size: 0.8em;
          }
          .add-btn {
            color: #ff9633;
            font-size: 0.6em;
            cursor: pointer;
            margin-top: 10px;
          }
        }
      }
    }
    .modal {
      .h {
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 30px;
      }
      .form {
        display: grid;
        grid-template-columns: 170px 100px 120px;
        & > div {
          margin: 10px;
        }
      }
      .template {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 10px;
        font-size: 0.9em;
      }
      .add-btn {
        background-color: #ff9633;
        font-weight: bold;
        padding: 10px;
        border-radius: 6px;
        margin-top: 20px;
        cursor: pointer;
        &.disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }
      }
    }
  }
</style>
