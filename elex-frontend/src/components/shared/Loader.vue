<template>
  <div class="shared_loader__wrapper">
    <div id="fountainG">
      <div id="fountainG_1" class="fountainG"></div>
      <div id="fountainG_2" class="fountainG"></div>
      <div id="fountainG_3" class="fountainG"></div>
      <div id="fountainG_4" class="fountainG"></div>
      <div id="fountainG_5" class="fountainG"></div>
      <div id="fountainG_6" class="fountainG"></div>
      <div id="fountainG_7" class="fountainG"></div>
      <div id="fountainG_8" class="fountainG"></div>
    </div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss">
  .shared_loader__wrapper {
    #fountainG{
      position:relative;
      width:234px;
      height:28px;
      margin:auto;
    }
    .fountainG{
      position:absolute;
      top:0;
      background-color:#ff9633;
      width:28px;
      height:28px;
      animation-name:bounce_fountainG;
      animation-duration:1.5s;
      animation-iteration-count:infinite;
      animation-direction:normal;
      transform:scale(.3);
      border-radius:19px;
    }
    #fountainG_1{
      left:0;
      animation-delay:0.6s;
    }
    #fountainG_2{
      left:29px;
      animation-delay:0.75s;
    }
    #fountainG_3{
      left:58px;
      animation-delay:0.9s;
    }
    #fountainG_4{
      left:88px;
      animation-delay:1.05s;
    }
    #fountainG_5{
      left:117px;
      animation-delay:1.2s;
    }
    #fountainG_6{
      left:146px;
      animation-delay:1.35s;
    }
    #fountainG_7{
      left:175px;
      animation-delay:1.5s;
    }
    #fountainG_8{
      left:205px;
      animation-delay:1.64s;
    }

    @keyframes bounce_fountainG{
      0%{
      transform:scale(1);
        background-color:#ff9633;
      }
      100%{
      transform:scale(.3);
        background-color:#ff9633;
      }
    }
  }
</style>
