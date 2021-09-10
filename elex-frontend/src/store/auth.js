import router from '../router';

export default {
  state: {
    user: {
      auth: false,
      name: '',
      admin: false,
      token: '',
    },
  },
  mutations: {
    setUser(state, user) {
      if (!user) {
        state.user.auth = false;
        state.user.name = '';
        state.user.admin = false;
        state.user.token = true;
      } else {
        state.user.auth = true;
        state.user.name = user.name;
        state.user.admin = user.isAdmin;
        state.user.token = user.token;
      }
    },
  },
  actions: {
    setUser({ commit }, payload = null) {
      if (payload) window.localStorage.setItem('token', payload.token);
      commit('setUser', payload);
      if (router.currentRoute.value.name === 'Auth') router.replace('/');
    },
  },
  getters: {
    getUser(state) {
      return state.user;
    },
  },
};
