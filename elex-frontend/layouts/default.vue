<template>
	<div class="layout_default__wrapper">
		<TheMenu />
		<Nuxt class="main-content" />
	</div>
</template>

<script>
import TheMenu from '~/components/base/TheMenu.vue';

export default {
	components: { TheMenu, },
}
</script>

<style lang="scss" scoped>
	.layout_default__wrapper {
		.main-content {
			margin-left: 275px;
		}
	}
</style>
