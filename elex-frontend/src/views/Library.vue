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
          :style="`grid-templates-rows: repeat(${getItemModifications(element.id).length}, 1fr)`">
          <div
            class="flex aic jcc"
            v-for="modification in getItemModifications(element.id)"
            :key="modification.id"
          >
            <div>{{ modification.name }}</div>
          </div>
        </div>
        <div class="special-row"
          :style="`grid-templates-rows: repeat(${getItemModifications(element.id).length}, 1fr)`">
          <div v-for="modification in getItemModifications(element.id)" :key="modification.id" >
            <div v-for="prop in getModificationsProperties(modification.id)" :key="prop.id"
              class="prop">
              {{ prop.name }} {{ prop.value }} {{ prop.dimension }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
  computed: {
    info() {
      return this.$store.getters.getInfo;
    },
  },
  methods: {
    getItemModifications(itemId) {
      return this.info.modifications.filter((m) => m.item === itemId);
    },
    getModificationsProperties(modId) {
      return this.info.properties.filter((p) => p.modification === modId);
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
          row-gap: 20px;
          & > div {
            overflow: scroll;
          }
          .prop {
            font-size: 0.8em;
          }
        }
      }
    }
  }
</style>
