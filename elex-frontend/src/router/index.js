import { createRouter, createWebHashHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Auth from '../views/Auth.vue';
import Library from '../views/Library.vue';
import Makers from '../views/Makers.vue';
import Types from '../views/Types.vue';
import Elements from '../views/Elements.vue';
import Modifications from '../views/Modifications.vue';
import PageNotFound from '../views/PageNotFound.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
  },
  {
    path: '/library',
    name: 'Library',
    component: Library,
  },
  {
    path: '/makers',
    name: 'Makers',
    component: Makers,
  },
  {
    path: '/types',
    name: 'Types',
    component: Types,
  },
  {
    path: '/elements',
    name: 'Elements',
    component: Elements,
  },
  {
    path: '/modifications',
    name: 'Modifications',
    component: Modifications,
  },
  {
    path: '/:catchAll(.*)',
    component: PageNotFound,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
