<template>
  <div class="shared_input__wrapper">
    <div class="placeholder">{{ placeholder }}</div>
    <input
      :type="password ? 'password' : 'text'"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    >
  </div>
</template>

<script>
export default {
  props: {
    placeholder: { type: String },
    password: { type: Boolean, default: false },
    modelValue: { type: String },
  },
};
</script>

<style lang="scss">
  .shared_input__wrapper {
    input[type="text"],
    input[type="password"] {
      background: none;
      outline: none;
      border-radius: none;
      border: none;
      border-bottom: 1px solid rgb(238, 131, 101);
      color: white;
      width: 100%;
      font-size: 1em;
      padding: 5px;
      &:-webkit-autofill,
      &:-webkit-autofill:hover,
      &:-webkit-autofill:focus,
      &:-webkit-autofill:active {
        box-shadow: 0 0 0 30px #1A1A1A inset;
        -webkit-text-fill-color: white;
      }
      &:-webkit-autofill::first-line {
        font-size: 16px;
      }
    }
    .placeholder {
      margin-top: 10px;
      margin-bottom: 5px;
      margin-left: 5px;
      font-size: 0.9em;
    }
  }
</style>
