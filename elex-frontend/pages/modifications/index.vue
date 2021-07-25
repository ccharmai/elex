<template>
	<div class="page_modifications__wrapper">
		<div class="controls">
			<div class="name">Производители</div>
			<div class="add" @click="add.show = true">Добавить +</div>
		</div>
		<table>
			<tr>
				<th>Компонент</th>
				<th>Название</th>
			</tr>
			<tr v-for="i in items" :key="i.index">
				<td>{{ i.name }}</td>
				<td>{{ i.item.name }}</td>
			</tr>
			<tr class="add" v-if="add.show">
				<td>
					<v-select v-model="add.item" placeholder="Компонент" :options="real_items" label="name" >
						<template #no-options>Нет компонентов</template>
					</v-select>
				</td>
				<td><input class="native-input" type="text" v-model="add.name"></td>
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
			item: '',
		},
		real_items: [],
	}},
	created() {
		this.$store.dispatch('setPreloader', true);
		axios.post(`${this.$store.getters.api}/get.modifications/`)
			.then(res => {
				if (res.data.status == 'ok') this.items = res.data.modifications;
				this.$store.dispatch('setPreloader', false);
			})
			.catch(err => {
				this.$store.dispatch('setPreloader', false);
			})

		axios.post(`${this.$store.getters.api}/get.items/`)
			.then(res => {
				if (res.data.status == 'ok') this.real_items = res.data.items;
			})
	},
	methods: {
		addItems() {
			if (this.add.name.length == 0 || !this.add.item) return ;
			let name = this.add.name;
			let item = this.add.item;
			this.add.name = ''; this.add.item = '';
			this.add.show = false;
			axios.post(`${this.$store.getters.api}/add.modifications/`, { name: name, item: item.id, token: this.$store.getters.getToken })
				.then(res => {
					if (res.data.status == 'ok') {
						if (res.data.visible) this.items.push({ id: res.data.id, name: name, item: item });
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
	.page_modifications__wrapper {
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
