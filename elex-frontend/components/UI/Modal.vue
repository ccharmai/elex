<template>
  <transition name="modal">
    <div class="modal__wrapper" @click="$emit('close')">
      <div class="modal-content" @click.stop="">
        <div class="modal-header">
          <span class="modal-title"> {{ title }} </span>
          <span class="button-close" @click="$emit('close')">×</span>
        </div>
        <div class="modal-body">
          <slot>Модальное окно</slot>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    }
  },
  data () {
    return {}
  },
  mounted () {
    document.body.addEventListener('keyup', e => {
      if (e.keyCode == 27)
        this.$emit('close');
    });
  },
  computed: {},
  methods: {}
}
</script>

<style lang="scss" scoped>
	// Animation
	.modal-enter, .modal-leave-active {
		opacity: 0;
	}
	.modal-enter .modal-content,
	.modal-leave-active .modal-content {
		transform: scale(1.2);
	}

	.modal__wrapper{
		display: flex;
		justify-content: center;
		align-items: center;
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		transition: opacity .2s ease;
		right: 0;
		z-index: 998;
		background-color: rgba(00,00,00,.48);
	}
	.modal-content {
		position: relative;
		max-width: 95vw;
		max-height: 95vh;
		padding: 20px 18px;
		background-color: #fff;
		border: 1px solid #dcdfe6;
		transition: all .2s ease;
		border-radius: 20px;
		z-index: 999;
		overflow: hidden;
		@media screen and (min-width: 900px) {
			min-width: 500px;
		}
	}
	.modal-header {
		display: flex;
		align-self: center;
		justify-content: space-between;
		padding-bottom: 20px;
		span {
			font-size: 24px;
		}
		.button-close {
			cursor: pointer;
			color: #FF4969;
		}
	}
	.modal-body {
		text-align: center;
	}

</style>
