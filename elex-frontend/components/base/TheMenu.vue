<template>
	<div class="base_menu__wrapper">
		<div class="menu-content">
			<nuxt-link to="/" class="nuxt-link">
				<div class="title-compose">
					<img src="/icon.png" alt="icon">
					<div class="title">ELEX</div>
				</div>
			</nuxt-link>
			<div class="menu-slot">

				<!-- no-auth-slot -->
				<div class="no-auth menu-list" v-if="!auth.isAuth">
					<div class="menu-item" v-for="(item, index) in noAuthSlot" :key="index">

						<nuxt-link :to="item.url" class="nuxt-link">
							<div class="link-compose">
								<div class="item-title">{{ item.title }}</div>
							</div>
						</nuxt-link>

					</div>
				</div>

				<!-- auth-slot -->
				<div class="no-auth menu-list" v-if="auth.isAuth">

					<nuxt-link to="/" class="nuxt-link menu-item">
						<div class="link-compose">Таблица</div>
					</nuxt-link>

					<nuxt-link to="/makers" class="nuxt-link  menu-item">
						<div class="link-compose">Производители</div>
					</nuxt-link>

					<nuxt-link to="/types" class="nuxt-link  menu-item">
						<div class="link-compose">Типы</div>
					</nuxt-link>

					<nuxt-link to="/items" class="nuxt-link  menu-item">
						<div class="link-compose">Элементы</div>
					</nuxt-link>

					<nuxt-link to="/modifications" class="nuxt-link  menu-item">
						<div class="link-compose">Модификации</div>
					</nuxt-link>

					<nuxt-link to="/properties" class="nuxt-link  menu-item">
						<div class="link-compose">Свойства</div>
					</nuxt-link>

				</div>

			</div>
		</div>
	</div>
</template>

<script>
export default {
	data() {return {
		noAuthSlot: [
			{
				title: 'Авторизация',
				action: 'nav',
				url: '/login',
			},
			{
				title: 'Компоненты',
				action: 'nav',
				url: '/',
			}
		],
		authSlot: [
			{
				title: 'hello',
				action: 'nav',
				url: 'cabinet/'
			},
			{
				title: 'Выход',
				action: 'nav',
				url: '/',
			},
		],
	}},
	computed: {
		auth() {
			return this.$store.getters.getAuth;
		}
	},
}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.base_menu__wrapper {
		height: 100vh;
		width: 275px;
		background-color: $primaryColor;
		position: fixed;
		top: 0;
		left: 0;
		.menu-content {
			width: 100%;
			height: 100%;
			padding: 25px;
		}
		.title-compose {
			display: flex;
			justify-content: center;
			img {
				width: 28px;
			}
			.title {
				margin-left: 10px;
			}
		}
		.menu-slot {
			margin-top: 40px;
		}
		.menu-item {
			border-bottom: 1px solid rgb(204, 204, 204);
			&:first-child {
				border-top: 1px solid rgb(204, 204, 204);
			}
			.link-compose {
				padding: 10px;
			}
		}
	}
</style>
