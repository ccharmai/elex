<template>
	<div class="ui_preloader__wrapper">
		<div class="preloader-component">
			<img src="/preloader.gif" alt="preloader gif">
		</div>
	</div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.ui_preloader__wrapper {
		width: 100vw;
		height: 100vh;
		position: fixed;
		top: 0;
		left: 0;
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: rgba(255, 255, 255, 0.5);
	}
</style>
