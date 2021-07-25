<template>
	<div class="page_properties__wrapper">
		<div class="controls">
			<div class="name">Типы компонентов</div>
			<div class="add" @click="add.show = true">Добавить +</div>
		</div>
		<table>
			<tr>
				<th>Модицикация</th>
				<th>Название</th>
				<th>Значение</th>
				<th>Размерность</th>
			</tr>
			<tr v-for="i in items" :key="i.index">
				<td>{{ i.modification.name }}</td>
				<td>{{ i.name }}</td>
				<td>{{ i.value }}</td>
				<td>{{ i.dimension }}</td>
			</tr>
			<tr class="add" v-if="add.show">
				<td>
					<v-select v-model="add.modification" placeholder="Модификация" :options="modifications" label="name" >
						<template #no-options>Нет модицикаций</template>
					</v-select>
				</td>
				<td><input class="native-input" type="text" v-model="add.name"></td>
				<td><input class="native-input" type="text" v-model="add.value"></td>
				<td><input class="native-input" type="text" v-model="add.dimension"></td>
				<div class="plus" @click="addItems()">+</div>
			</tr>
		</table>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {return {
		items: [],
		add: {
			show: false,
			name: '',
			value: '',
			dimension: '',
			modification: '',
		},
		modifications: [],
	}},
	created() {
		this.$store.dispatch('setPreloader', true);
		axios.post(`${this.$store.getters.api}/get.properties/`)
			.then(res => {
				if (res.data.status == 'ok') this.items = res.data.properties;
				this.$store.dispatch('setPreloader', false);
			})
			.catch(err => {
				this.$store.dispatch('setPreloader', false);
			})

		axios.post(`${this.$store.getters.api}/get.modifications/`)
			.then(res => {
				if (res.data.status == 'ok') this.modifications = res.data.modifications;
			})
	},
	methods: {
		addItems() {
			if (this.add.name.length == 0 || this.add.value.length == 0 || this.add.dimension.length == 0 || !this.add.modification) return ;
			let name = this.add.name;
			let value = this.add.value;
			let dimension = this.add.dimension;
			let modification = this.add.modification;
			this.add.name = ''; this.add.value = ''; this.add.dimension = ''; this.add.dimension = '';
			this.add.show = false;
			axios.post(`${this.$store.getters.api}/add.properties/`, { name: name, value: value, dimension: dimension, modification: modification.id, token: this.$store.getters.getToken })
				.then(res => {
					if (res.data.status == 'ok') {
						if (res.data.visible) this.items.push({ id: res.data.id, name: name, value: value, dimension: dimension, modification: modification });
						else this.$toast.success('Запись отправлена на модерацию');
					}
					else {
						if (res.data.msg) this.$toast.error(res.data.msg);
						else this.$toast.error('Ошибка добавления');
					}
				})
				.catch((err) => {
					this.$toast.error('Ошибка запроса к серверу')
				})
		}
	}
}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.page_properties__wrapper {
		padding: 20px;
		.controls {
			display: flex;
			justify-content: space-between;
			align-items: center;
			.add {
				background: rgb(199, 198, 198);
				padding: 15px;
				border-radius: 100px;
				cursor: pointer;
			}
		}
		table {
			margin-top: 20px;
			.add {
				position: relative;
				.plus {
					position: absolute;
					font-size: 35px;
					right: 15px;
					top: calc(50% - 22px);
					color: green;
					cursor: pointer;
				}
				.native-input {
					outline: none;
					border: none;
					padding: 10px;
					border-radius: 0;
				}
			}
		}
	}
</style>
