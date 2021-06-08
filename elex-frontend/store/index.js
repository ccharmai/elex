import axios from 'axios';
import Cookie from 'js-cookie';

export const state = () => ({
	auth: {
		isAuth: false,
		name: '',
		isAdmin: false,
		token: '',
		loaded: false,
	},
	preloader: false,
})

export const mutations = {

	setAuth(state, payload) {
		state.auth.isAuth = payload.isAuth;
		state.auth.name = payload.name;
		state.auth.isAdmin = payload.isAdmin;
		state.auth.token = payload.token;
	},

	setAuthLoaded(state) {
		state.auth.loaded = true;
	},

	setPreloader(state, payload) {
		state.preloader = payload;
	}
}

export const actions = {

	init({commit, getters}, payload) {

		// check auth part
		// Если у нас есть токен, то сохраняем всю информацию о пользователе в state

		let cookieToken = Cookie.get('token');
		console.log(cookieToken)
		if (cookieToken) {
			// get info about token from server
			axios.post(`${getters.api}/token.info/`, { token: cookieToken })
				.then(res => {
					console.log(res.data)
					if (res.data.status != 'ok') return ;
					commit('setAuth', {
						isAuth: true,
						name: res.data.name,
						isAdmin: res.data.isAmin,
						token: cookieToken
					});
					commit('setAuthLoaded');
				})
		}
		else {
			commit('setAuthLoaded');
		}
	},

	login({commit}, payload) {
		commit('setAuth', { isAuth: true, ...payload });
		Cookie.set('token', payload.token);
	},

	setPreloader({commit}, payload) {
		commit('setPreloader', payload);
	}
}

export const getters = {
	api(state) {
		return 'http://localhost:8000/api';
	},
	getAuth(state) {
		return state.auth;
	},
	getPreloader(state) {
		return state.preloader;
	},
}
