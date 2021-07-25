<template>
	<div class="page_items__wrapper">
		<div class="controls">
			<div class="name">Типы компонентов</div>
			<div class="add" @click="add.show = true">Добавить +</div>
		</div>
		<table>
			<tr>
				<th>Производитель</th>
				<th>Тип</th>
				<th>Имя</th>
			</tr>
			<tr v-for="i in items" :key="i.index">
				<td>{{ i.maker.name }}</td>
				<td>{{ i.type.name }}</td>
				<td>{{ i.name }}</td>
			</tr>
			<tr class="add" v-if="add.show">
				<td>
					<v-select v-model="add.maker" placeholder="Производитель" :options="makers" label="name" >
						<template #no-options>Нет производителей</template>
					</v-select>
				</td>
				<td>
					<v-select v-model="add.type" placeholder="Тип" :options="types" label="name" >
						<template #no-options>Нет типов</template>
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
			maker: '',
			type: '',
		},
		makers: [],
		types: [],
	}},
	created() {
		this.$store.dispatch('setPreloader', true);
		axios.post(`${this.$store.getters.api}/get.items/`)
			.then(res => {
				if (res.data.status == 'ok') this.items = res.data.items;
				this.$store.dispatch('setPreloader', false);
			})
			.catch(err => {
				this.$store.dispatch('setPreloader', false);
			})

		axios.post(`${this.$store.getters.api}/get.makers/`)
			.then(res => {
				if (res.data.status == 'ok') this.makers = res.data.makers;
			})

		axios.post(`${this.$store.getters.api}/get.types/`)
			.then(res => {
				if (res.data.status == 'ok') this.types = res.data.types;
			})
	},
	methods: {
		addItems() {
			if (this.add.name.length == 0 || !this.add.maker || !this.add.type) return ;
			let name = this.add.name;
			let maker = this.add.maker;
			let type = this.add.type;
			this.add.name = ''; this.add.maker = ''; this.add.type = '';
			this.add.show = false;
			axios.post(`${this.$store.getters.api}/add.items/`, { name: name, maker: maker.id, type: type.id, token: this.$store.getters.getToken })
				.then(res => {
					if (res.data.status == 'ok') {
						if (res.data.visible) this.items.push({ id: res.data.id, name: name, maker: maker, type: type });
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
	.page_items__wrapper {
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
