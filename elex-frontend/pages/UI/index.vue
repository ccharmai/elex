<template>
	<div class="test_page__wrapper">
		<div class="wrapper">

			<div class="title">Заголовок</div>

			<div>Не заголовок</div>

			<div><Button text="Кнопка" @click="click()"/></div>

			<div><Button text="Кнопка заблокирована" disabled @click="click()"/></div>

			<div style="margin-top: 10px;">
				<v-select v-model="selectedModel" placeholder="Опции" :options="['Апельсин', 'Яблоко', 'Арбуз']" >
					<template #no-options>
      					Нет подходящих опций
   					</template>
				</v-select>
			</div>
			<div style="margin-top: 10px; color: grey;" v-if="selectedModel">Выбранная опция: {{ selectedModel }}</div>

			<div style="margin-top: 10px;">
				<v-select v-model="currentToast" placeholder="Выберите тип уведомления" :options="['success', 'info', 'error', 'warning']" >
					<template #no-options>
      					Нет подходящих опций
   					</template>
				</v-select>
			</div>
			<div><Button text="Уведомление" @click="showToasts()" /></div>

			<input type="text" v-model="line" />
			<div style="margin-top: 10px; color: grey;" v-if="line">Введен текст: {{ line }}</div>

			<div>Количество элементов в таблице: <input onkeydown="return false" min=0 max=10 v-model="countElementsInTable" style="margin-left: 10px; width: 100px;" type="number" /></div>
			<table style="margin-top: 20px;">
				<tr>
					<th>Название</th>
					<th>Тип</th>
					<th>Вес (г.)</th>
				</tr>
				<tr v-for="i in parseInt(countElementsInTable)" :key="i">
					<td>AP-12</td>
					<td>Резистор</td>
					<td>110</td>
				</tr>
			</table>

			<Modal v-if="showModalWindow" @close="showModalWindow = false">
				<slot>Модальное окно</slot>
			</Modal>
			<Button text="Показать модальное окно" @click="showModalWindow = true"/>
		</div>
	</div>
</template>

<script>
import Button from '~/components/UI/Button.vue'
export default {
	components: { Button },
	data() {return {
		selectedModel: '',
		currentToast: '',
		line: '',
		countElementsInTable: 4,
		showModalWindow: false,
	}},
	methods: {
		click() {
			console.log('click');
		},
		showToasts() {
			if (this.currentToast == 'success') this.$toast.success("Success notify");
			if (this.currentToast == 'info') this.$toast.info("Info notify");
			if (this.currentToast == 'error') this.$toast.error("Error notify");
			if (this.currentToast == 'warning') this.$toast.warning("Warning notify");
			this.currentToast = '';
		},
	},
}
</script>

<style lang="scss">
	@import "~/assets/scss/vars.scss";
	.test_page__wrapper {
		.wrapper {
			margin-top: 20px;
		}
	}
</style>
