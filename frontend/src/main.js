import { createApp } from 'vue';
import loader from 'vue-ui-preloader';
import App from './App.vue';
import router from './router';
import store from './store';
import './assets/style.scss';

createApp(App).use(store).use(router).use(loader)
  .mount('#app');
