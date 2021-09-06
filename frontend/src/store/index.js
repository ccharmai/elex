import { createStore } from 'vuex';

export default createStore({
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
    showPagePreloader(state) {
      return state.showPagePreloader;
    },
  },
});
