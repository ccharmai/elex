<template>
  <div class="settings_password_settings__wrapper">
    <div class="settings-title">Настройки пароля</div>
    <div class="change-password">
      <div class="form" @keyup.enter="changeHandler">
        <Input password v-model="newPassword" placeholder="Новый пароль" />
        <Input password v-model="newPasswordRepeat" placeholder="Новый пароль еще раз" />
        <div class="btn" :class="{ 'disabled': !canChangePassword }"
          @click="changeHandler"
        >
          Сменить пароль
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

import Input from '@/components/shared/Input.vue';

export default {
  components: {
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
      newPassword: '',
      newPasswordRepeat: '',
    };
  },
  methods: {
    changeHandler() {
      if (!this.canChangePassword) return;
      const { token } = this.$store.getters.getUser;
      const apiUrl = `${this.$store.getters.api}/person.change_password/`;
      axios.post(apiUrl, { token, password: this.newPassword })
        .then((res) => {
          if (res.data.status === 'ok') {
            this.newPassword = '';
            this.newPasswordRepeat = '';
            this.toast.success('Пароль успешно изменен!');
          }
        })
        .catch((err) => {
          console.warn(err);
        });
    },
  },
  computed: {
    canChangePassword() {
      return this.newPassword.length > 0 && this.newPassword === this.newPasswordRepeat;
    },
  },
};
</script>

<style lang="scss">
  .settings_password_settings__wrapper {
    .form {
      width: 80%;
      margin: 0 auto;
      margin-top: 50px;
      .btn {
        margin-top: 40px;
        background: rgb(238, 131, 101);
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        font-weight: normal;
        text-align: center;
        &.disabled {
          cursor: not-allowed;
          opacity: .4;
        }
      }
    }
  }
</style>
