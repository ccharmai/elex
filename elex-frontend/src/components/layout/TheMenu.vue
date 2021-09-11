<template>
  <div class="layout_the_menu__wrapper">
    <div class="logo" @click="$router.push('/')">Elex<span>.</span></div>
    <div class="menu-items" v-if="user.auth">
      <router-link to="/"
        class="menu-item"
        :class="{ 'current': pageName === 'Dashboard' }"
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
    <div class="menu-items" v-if="!user.auth">
      <router-link to="/auth"
        class="menu-item"
        :class="{ 'current': pageName === 'Auth' }"
      >Login</router-link>
    </div>
    <div class="account" v-show="user.auth">
      <div class="mini">
        <transition name="bounce">
          <MiniMenu v-show="showMiniMenu" @close="showMiniMenu = false" />
        </transition>
      </div>
      <div class="icon">{{ user.auth ? user.name[0].toUpperCase() : '' }}</div>
      <div class="text">
        <div class="name">{{ user.auth ? user.name : '' }}</div>
        <div class="status">{{ user.auth ? user.admin ? 'Admin' : 'User' : 'Anonymous' }}</div>
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
    user() {
      return this.$store.getters.getUser;
    },
  },
  mounted() {
    // register click outside mini menu and current menu
    const miniMenu = document.querySelector('.layout_the_menu__wrapper .mini');
    const menu = document.querySelector('.layout_the_menu__wrapper .account');
    document.addEventListener('click', (e) => {
      if (!menu.contains(e.target) && !miniMenu.contains(e.target)) this.showMiniMenu = false;
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
      cursor: pointer;
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
