<template>
  <div class="page_auth__wrapper" :class="{ 'wait': loading }">
    <div class="container">
      <div class="logo"></div>
      <div class="form" @keyup.enter="loginHandler()">
        <Input v-model="login" placeholder="Логин" />
        <Input v-model="password" placeholder="Пароль" password />
      </div>
      <div class="btn__wrapper">
        <div class="btn" @click="loginHandler()">Войти</div>
      </div>
      <div class="help" @click="showCreateModal = true">Заявка на создание аккаунта</div>
    </div>
    <Modal v-show="showCreateModal" @close="showCreateModal = false">
      <div class="modal-slot">
        <div class="head">Заявка на аккаунт Elex</div>
        <div class="body">
          <Input v-model="newlogin" placeholder="Логин" />
          <Input v-model="newpassword" placeholder="Пароль" password />
          <div class="placeholder">Сопроводительное письмо</div>
          <textarea v-model="newdescription"></textarea>
          <div class="btn" @click="createHandler()">Отправить</div>
        </div>
      </div>
    </Modal>
  </div>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';
import Input from '@/components/shared/Input.vue';
import Modal from '@/components/shared/Modal.vue';

export default {
  components: {
    Input,
    Modal,
  },
  setup() {
    const toast = useToast();
    return { toast };
  },
  data() {
    return {
      login: '',
      password: '',
      loading: false,
      showCreateModal: false,
      newLoading: false,
      newlogin: '',
      newpassword: '',
      newdescription: '',
    };
  },
  methods: {
    loginHandler() {
      if (this.loading || !this.canLogin) return;
      this.loading = true;
      const loginUrl = `${this.$store.getters.api}/token.get/`;
      axios.post(loginUrl, { name: this.login, password: this.password })
        .then((res) => {
          if (res.data.status !== 'ok') {
            this.toast.error(res.data.msg);
          } else {
            this.toast.success('Авторизация выполнена');
            this.$store.dispatch('setUser', { ...res.data });
            this.$router.push('/');
          }
          this.loading = false;
        })
        .catch((err) => {
          console.log(err);
          this.loading = false;
        });
    },
    createHandler() {
      if (this.newLoading || this.newlogin.length === 0 || this.newpassword.length === 0) return;
      const createUrl = `${this.$store.getters.api}/person.create/`;
      this.newLoading = true;
      axios.post(createUrl, { name: this.newlogin, password: this.newpassword })
        .then((res) => {
          if (res.data.status !== 'ok') {
            this.toast.error(res.data.msg);
          }
          if (res.data.status === 'ok') {
            this.toast.success('Заявка успешно создана');
            this.showCreateModal = false;
            this.newlogin = '';
            this.newpassword = '';
          }
          this.newLoading = false;
        })
        .catch((err) => {
          console.log(err);
          this.newLoading = false;
        });
    },
  },
  computed: {
    canLogin() {
      return this.login.length > 0 && this.password.length > 0;
    },
    user() {
      return this.$store.getters.getUser;
    },
  },
  created() {
    if (this.user.auth) this.$router.replace('/');
  },
};
</script>

<style lang="scss">
  .page_auth__wrapper {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    &.wait {
      cursor: wait !important;
      .btn { cursor: wait !important; }
    }
    .container {
      width: 300px;
      height: 450px;
      background: #1A1A1A;
      border-radius: 25px;
      box-shadow: 0 0 20px 0 #1A1A1AB3;
      padding: 30px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .logo {
      width: 50px;
      height: 50px;
      border-radius: 10px;
      background: rgb(238, 131, 101);
      margin: 0 auto;
    }
    .btn__wrapper {
      display: flex;
      justify-content: center;
      .btn {
        background: rgb(238, 131, 101);
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        font-weight: normal;
      }
    }
    .help {
      font-size: 0.8em;
      text-align: center;
      margin-top: 40px;
      color: #737373;
      cursor: pointer;
    }
    .modal-slot {
      textarea {
        background: none;
        outline: none;
        border: 1px solid rgb(238, 131, 101);
        width: 500px;
        height: 200px;
        font-size: 1em;
        padding: 15px;
        color: white;
        resize: none;
      }
      .placeholder {
        font-size: 0.9em;
        margin-top: 20px;
        margin-bottom: 10px;
      }
      .btn {
        text-align: center;
        padding: 10px;
        margin-top: 20px;
        background: rgb(238, 131, 101);
        border-radius: 10px;
        cursor: pointer;
      }
    }
  }
</style>
