<template>
	<div class="page_main__wrapper">
		<div class="wrapper">
			<!--<nuxt-link to="/UI">Библиотека компонентов</nuxt-link>-->
			{{ table }}
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {return {
		table: '',
	}},
	created() {
		axios.post(`${this.$store.getters.api}/get.table/`)
			.then(res => {
				if (res.data.status == 'ok') this.table = res.data.table;
			})
	}
}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.page_main__wrapper {
		.wrapper {
			margin-top: 20px;
		}
	}
</style>
