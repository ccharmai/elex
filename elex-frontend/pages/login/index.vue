<template>
	<div class="page_login__wrapper">
		<div class="login-window">
			<div class="title">Авторизация в <span class="text-logo">ELEX</span></div>
			<div class="form">
				<div class="form-item">
					<label for="name">Имя</label>
					<input v-model="name" type="text">
				</div>
				<div class="form-item">
					<label for="name">Пароль</label>
					<input v-model="password" type="password">
				</div>
				<div class="center__container">
					<Button :disabled="!name || !password" @click="login()" class="btn" text="Войти" />
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {return {
		name: '',
		password: '',
	}},
	methods: {
		login() {
			if (!this.name || !this.password) return ;
			this.$store.dispatch('setPreloader', true);
			axios.post(`${this.$store.getters.api}/token.get/`, { name: this.name, password: this.password })
				.then(res => {
					this.$store.dispatch('setPreloader', false);
					if (res.data.status == 'ok') {
						// login here
						this.$toast.success('Вход выполнен успешно!');
						this.$store.dispatch('login', { name: res.data.name, isAdmin: res.data.isAdmin, token: res.data.token });
					}
					else {
						this.$toast.error(res.data.msg);
					}
				})
				.catch(err => {
					this.$store.dispatch('setPreloader', false);
				})
		},
	}
}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.page_login__wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: 100vh;
		.login-window {
			padding: 20px;
			border-radius: 20px;
			width: 550px;
			min-height: 250px;
			background: white;
			box-shadow: 0px 0px 20px 2px #0000001a;
		}
		.title {
			text-align: center;
			.text-logo {
				color: $primaryColor;
				font-size: 110%;
			}
		}
		.form {
			margin: 0 auto;
			margin-top: 30px;
			width: 80%;
			.btn {
				margin-top: 30px;
			}
		}
		.form-item {
			margin-top: 25px;
			width: 100%;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}
	}
</style>
