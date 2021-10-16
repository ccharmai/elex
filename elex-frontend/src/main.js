import { createApp } from 'vue';
import loader from 'vue-ui-preloader';
import Toast, { POSITION } from 'vue-toastification';
import SlideUpDown from 'vue3-slide-up-down';
import App from './App.vue';
import router from './router';
import store from './store';
import './assets/style.scss';
import 'vue-toastification/dist/index.css';

createApp(App)
  .use(store)
  .use(router)
  .use(loader)
  .use(Toast, {
    position: POSITION.TOP_RIGHT,
  })
  .component('slide-up-down', SlideUpDown)
  .mount('#app');
