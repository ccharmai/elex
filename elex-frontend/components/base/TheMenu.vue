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
				<div class="no-auth menu-list">
					<div class="menu-item" v-for="(item, index) in noAuthSlot" :key="index">
						<nuxt-link :to="item.url" class="nuxt-link">
							<div class="link-compose">
								<div class="icon"><img v-if="item.icon" :src="item.icon" alt="menu icon"></div>
								<div class="item-title">{{ item.title }}</div>
							</div>
						</nuxt-link>
					</div>
				</div>
				<!-- auth-slot -->
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
				icon: '/icons/enter.png',
				url: '/login',
			},
		],
	}},
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
			padding: 10px;
			.link-compose {
				$iconSize: 20px;
				display: flex;
				justify-content: space-between;
				.icon, .icon img {
					width: $iconSize;
					height: $iconSize;
				}
				.item-title {
					margin-left: 10px;
				}
			}
		}
	}
</style>
