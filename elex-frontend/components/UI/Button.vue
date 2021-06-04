<template>
	<div class="ui_button__wrapper" :class="{'disabled': disabled}" @click="click">
		<div class="text">{{ text }}</div>
	</div>
</template>

<script>
export default {
	props: {
		text: { type: String },
		disabled: { type: Boolean, default: false },
	},
	methods: {
		click() {
			if (!this.disabled) this.$emit('click');
		}
	},
}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.ui_button__wrapper {
		background-color: $primaryColor;
		display: inline-block;
		padding: 10px 20px;
		border-radius: 10px;
		cursor: pointer;
		transition: .3s ease-in-out background;
		margin: 5px 0;
		&:hover {
			background-color: $primaryColorDark;
		}
		&.disabled {
			background-color: $grey;
			cursor: not-allowed;
			opacity: .5;
			&:hover {
				background-color: $grey;
			}
		}
		.text {
			color: #fff;
			user-select: none;
			font-size: 90%;
		}
	}
</style>
