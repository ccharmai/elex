import { createStore } from 'vuex';
import auth from './auth';
import table from './table';

export default createStore({
  modules: {
    auth,
    table,
  },
  state: {
    showPagePreloader: true,
  },
  mutations: {
    setPreloader(state, preloader) {
      state.showPagePreloader = preloader;
    },
  },
  actions: {
    setPreloader({ commit, getters }, payload) {
      if (!payload) commit('setPreloader', !getters.showPagePreloader);
      else commit('setPreloader', payload);
    },
  },
  getters: {
    api() {
      return 'http://127.0.0.1:8000/api';
    },
    showPagePreloader(state) {
      return state.showPagePreloader;
    },
  },
});
