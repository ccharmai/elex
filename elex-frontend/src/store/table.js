/* eslint-disable */
import axios from 'axios';

export default {
  state: {
    info: {
      loading: true,
      makers: [],
      types: [],
      elements: [],
      modifications: [],
      properties: [],
    },
  },
  mutations: {
    setLoading(state, loading = true) {
      state.info.loading = loading;
    },
    setField(state, data) {
      state.info[data.field] = data.value;
    },
  },
  actions: {
    initData({ commit, dispatch }) {
      commit('setLoading', true);
      dispatch('getAllData');
    },
    getAllData({ commit, getters }) {
      let countLoadingFields = 0; // expected 4 (fields.length)
      const fields = ['makers', 'types', 'elements', 'modifications', 'properties'];
      const { token } = getters.getUser;
      const url = `${getters.api}/get.`;
      for (const field of fields) {
        axios.post(`${url}${field}/`, { token })
          .then((res) => {
            if (res.data.status === 'ok') commit('setField', { field: field, value: res.data.objects });
            else console.warn('Error in server response', res.data);
          })
          .catch((err) => { console.warn(err); })
          .finally(() => {
            countLoadingFields += 1;
            if (countLoadingFields === fields.length) commit('setLoading', false);
          });
      }
    },
  },
  getters: {
    getInfo(state) {
      return state.info;
    },
  },
};
