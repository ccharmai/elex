export default {
  state: {
    user: {
      auth: false,
      name: '',
      admin: false,
      token: '',
    },
  },
  mutations: {},
  actions: {},
  getters: {
    getUser(state) {
      return state.user;
    },
  },
};
