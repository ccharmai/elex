<template>
  <div class="settings_moderation_list__wrapper">
    <div class="block" @click="isExpanded = !isExpanded">
      <div class="text">{{ name }}</div>
      <div class="expand" :class="{ 'expanded': isExpanded }">
        <img src="@/assets/img/arrow.svg" />
      </div>
    </div>
    <slide-up-down v-model="isExpanded" :duration="50">
      <div class="expanded-content">
        <div v-if="loading" class="loading">Loading...</div>
        <div v-else-if="list.length === 0" class="no-items">Нет элементов</div>
        <table v-else class="list">
          <tr class="list-header">
            <template v-if="name === 'Properties'">
              <td>Id</td>
              <td>Modification</td>
              <td>Name</td>
              <td>Value</td>
              <td>Dimension</td>
            </template>
            <template v-if="name === 'Makers' || name === 'Types'">
              <td>Id</td>
              <td>Name</td>
              <td>Description</td>
            </template>
            <template v-if="name === 'Elements'">
              <td>Id</td>
              <td>Maker</td>
              <td>Type</td>
              <td>Name</td>
            </template>
            <template v-if="name === 'Modifications'">
              <td>Id</td>
              <td>Item</td>
              <td>Name</td>
            </template>
            <td></td>
            <td></td>
          </tr>
          <tr class="list-item" v-for="item in list" :key="item.id">
            <template v-if="name === 'Properties'">
              <td>{{ item.id }}</td>
              <td>{{ info.modifications.find(m => m.id === item.modification)?.name ?? item.modification }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.value }}</td>
              <td>{{ item.dimension }}</td>
            </template>
            <template v-if="name === 'Makers' || name === 'Types'">
              <td>{{ item.id }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.description }}</td>
            </template>
            <template v-if="name === 'Elements'">
              <td>{{ item.id }}</td>
              <td>{{ info.makers.find(m => m.id === item.maker)?.name ?? item.maker }}</td>
              <td>{{ info.types.find(m => m.id === item.type)?.name ?? item.type }}</td>
              <td>{{ item.name }}</td>
            </template>
            <template v-if="name === 'Modifications'">
              <td>{{ item.id }}</td>
              <td>{{ info.elements.find(m => m.id === item.item)?.name ?? item.item }}</td>
              <td>{{ item.name }}</td>
            </template>
            <td @click="onControlClick('approve', item.id)"><img class="ok" src="@/assets/img/ok.svg" /></td>
            <td @click="onControlClick('discard', item.id)"><img class="delete" src="@/assets/img/delete.svg" /></td>
          </tr>
        </table>
      </div>
    </slide-up-down>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    name: String,
  },
  data() {
    return {
      isExpanded: false,
      list: [],
      loading: false,
    };
  },
  created() {
    const url = `${this.$store.getters.api}/get.${this.name.toLowerCase()}/`;
    const { token } = this.$store.getters.getUser;
    this.loading = true;
    axios.post(url, { token, invisible: true })
      .then((res) => {
        if (res.data.status === 'ok') this.list = res.data.objects.filter((o) => !o.is_visible);
      })
      .finally(() => {
        this.loading = false;
      });
  },
  computed: {
    info() {
      return this.$store.getters.getInfo;
    },
  },
  methods: {
    onControlClick(buttonType, itemId) {
      if (!['approve', 'discard'].includes(buttonType)) return;
      const url = `${this.$store.getters.api}/adm/set/`;
      const { token } = this.$store.getters.getUser;
      axios.post(url, {
        token, field: this.name, action: buttonType, id: itemId,
      })
        .then((res) => {
          if (res.data.status === 'ok') {
            this.list = this.list.filter((l) => l.id !== itemId);
          }
        });
    },
  },
};
</script>

<style lang="scss">
  .settings_moderation_list__wrapper {
    margin-top: 20px;
    .block {
      width: 100%;
      padding: 15px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background-color: #171717;
      border-radius: 10px;
      cursor: pointer;
      .expand {
        user-select: none;
        display: flex;
        align-items: center;
        width: 15px;
        transition: .1s ease-in-out transform;
        transform: rotate(180deg);
        &.expanded {
          transform: none;
        }
      }
    }
    .expanded-content {
      margin-top: 10px;
      border-radius: 10px;
      padding: 15px 20px;
      background-color: #282828;
    }
    .list {
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
      .list-item {
        .ok, .delete {
          width: 15px;
          position: relative;
          top: 4px;
          cursor: pointer;
        }
      }
    }
  }
</style>
