<template>
	<div class="layout_default__wrapper">
		<TheMenu />
		<Nuxt class="main-content" />
		<Preloader v-if="showPreloader" />
	</div>
</template>

<script>
import TheMenu from '~/components/base/TheMenu.vue';
import Preloader from '~/components/UI/Preloader.vue';

export default {
	components: { TheMenu, Preloader, },
	created() {
		// store init (For example - get users settings from cookie)
		this.$store.dispatch('init');
	},
	computed: {
		showPreloader() {
			return this.$store.getters.getPreloader;
		}
	},
}
</script>

<style lang="scss" scoped>
	.layout_default__wrapper {
		.main-content {
			margin-left: 275px;
		}
	}
</style>
