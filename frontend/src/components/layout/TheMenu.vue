<template>
  <div class="layout_the_menu__wrapper">
    <div class="logo">Elex<span>.</span></div>
    <div class="menu-items">
      <router-link to="/"
        class="menu-item"
        :class="{ 'current': pageName === 'Home' }"
      >Dashboard</router-link>
      <router-link to="/library"
        class="menu-item"
        :class="{ 'current': pageName === 'Library' }"
      >Library</router-link>
      <router-link to="/makers"
        class="menu-item"
        :class="{ 'current': pageName === 'Makers' }"
      >Makers</router-link>
      <router-link to="/types"
        class="menu-item"
        :class="{ 'current': pageName === 'Types' }"
      >Types</router-link>
      <router-link to="/elements"
        class="menu-item"
        :class="{ 'current': pageName === 'Elements' }"
      >Elements</router-link>
      <router-link to="/modifications"
        class="menu-item"
        :class="{ 'current': pageName === 'Modifications' }"
      >Modifications</router-link>
    </div>
    <div class="account">
      <div class="mini">
        <transition name="bounce">
          <MiniMenu v-show="showMiniMenu" />
        </transition>
      </div>
      <div class="icon">S</div>
      <div class="text">
        <div class="name">Sergey</div>
        <div class="status">User</div>
      </div>
      <div class="nav" @click="showMiniMenu = !showMiniMenu">
        <img src="../../assets/img/nav.svg" alt="Nav buttons">
      </div>
    </div>
  </div>
</template>

<script>
import MiniMenu from '@/components/layout/MiniMenu.vue';

export default {
  components: {
    MiniMenu,
  },
  data() {
    return {
      showMiniMenu: false,
    };
  },
  computed: {
    pageName() {
      return this.$route.name;
    },
  },
  mounted() {
    // register click outside mini menu and current menu
    document.addEventListener('click', (e) => {
      if (!this.$el.contains(e.target)) this.showMiniMenu = false;
    });
  },
};
</script>

<style lang="scss">
  .layout_the_menu__wrapper {
    width: 275px;
    min-width: 275px;
    background-color: #1A1A1A;
    height: 100vh;
    box-shadow: 0 0 3px 0px #e4e4e41a;
    display: flex;
    flex-direction: column;
    .logo {
      padding: 30px;
      font-size: 2.5em;
      span {
        color: rgb(238, 131, 101);
      }
    }
    .menu-items {
      margin-top: 30px;
      .menu-item {
        display: block;
        color: white;
        text-decoration: none;
        width: 90%;
        padding: 15px 20px;
        cursor: pointer;
        font-weight: 600;
        transition: .3 ease-in-out background;
        &.current {
          background-color: #3F8CFF;
          border-radius: 0px 12px 12px 0px;
        }
      }
    }
    .account {
      margin-top: auto;
      padding: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      .icon {
        width: 40px;
        height: 40px;
        border-radius: 20px;
        background-color: rgb(238, 131, 101);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
      }
      .text {
        .name {
          font-weight: 600;
        }
        .status {
          color: #808191;
        }
      }
      .nav {
        cursor: pointer;
      }
      .mini {
        position: absolute;
        bottom: 100%;
        left: 10%;
        right: 10%;
        width: 80%;
      }
    }
  }
</style>
