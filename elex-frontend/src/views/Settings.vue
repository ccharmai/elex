<template>
  <div class="page_settings__wrapper">
    <div class="settings-list">
      <div class="items__wrapper" @click="currentPage = ''">
        <template v-if="user.auth && user.admin">
          <div class="item" v-for="i in adminSettings" :key="i.name"
            @click.stop="currentPage = i.name"
            :class="{ 'current': currentPage === i.name }"
          >
            <div class="text">{{ i.label }}</div>
          </div>
        </template>
        <div class="item" v-for="i in settings" :key="i.name"
          @click.stop="currentPage = i.name"
          :class="{ 'current': currentPage === i.name }"
        >
          <div class="text">{{ i.label }}</div>
        </div>
      </div>
    </div>
    <div class="settings-content">
      <PasswordSettings v-show="currentPage === 'password'" />
    </div>
  </div>
</template>

<script>
import PasswordSettings from '@/components/settings/PasswordSettings.vue';

export default {
  components: {
    PasswordSettings,
  },
  created() {
    if (!this.$store.getters.getUser.auth) this.$router.push('/auth');
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    },
  },
  data() {
    return {
      currentPage: '',
      settings: [
        {
          name: 'password',
          label: 'Пароль',
        },
      ],
      adminSettings: [
        {
          name: 'users',
          label: 'Пользователи',
        },
      ],
    };
  },
};
</script>

<style lang="scss">
  .page_settings__wrapper {
    height: 100%;
    display: flex;
    .settings-list {
      margin: -20px;
      $width: 250px;
      width: $width;
      min-width: $width;
      max-width: $width;
      height: calc(100% + 40px);
      background: #171717;
      .items__wrapper {
        height: 100%;
        padding-top: 40px;
        padding-bottom: 40px;
        box-shadow: inset 0px 0px 10px #0a0a0a80;
        .item {
          padding: 10px;
          padding-left: 15px;
          height: 50px;
          border-top: 1px solid #292929;
          cursor: pointer;
          display: flex;
          align-items: center;
          transition: .1s ease-in-out background;
          &:last-child {
            border-bottom: 1px solid #292929;
          }
          .text {
            color: #717171;
          }
          &.current {
            background: #131313;
          }
        }
      }
    }
    .settings-content {
      margin-left: 40px;
      width: 100%;
      height: 100%;
      flex-grow: 1;
    }
  }
</style>
