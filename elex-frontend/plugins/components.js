import Vue from 'vue'

import Button from '~/components/UI/Button.vue'
Vue.component('Button', Button)

import Modal from '~/components/UI/Modal.vue'
Vue.component('Modal', Modal)

import vSelect from "vue-select";
import 'vue-select/dist/vue-select.css';
Vue.component("v-select", vSelect);

import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
Vue.use(Toast, { position: 'top-right' });
