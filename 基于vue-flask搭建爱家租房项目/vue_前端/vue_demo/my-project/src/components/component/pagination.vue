<template>
  <div class="swiper-container swiper-no-swiping swiper-container-horizontal" id="bannerSwiper">
    <div class="swiper-wrapper">
      <div class="swiper-slide">
        <p class="contents"><i class="fa fa-home" aria-hidden="false"></i>&nbsp;二手房</p>
        <p class="text">链家网越来越懂你</p>
        <lubo1></lubo1>
      </div>
      <div class="swiper-slide">
        <p class="contents"><i class="fa fa-home" aria-hidden="false"></i>&nbsp;新房</p>
        <p class="text">新起航,最新资讯一手掌握</p>
        <lubo2></lubo2>
      </div>
      <div class="swiper-slide">
        <p class="contents"><i class="fa fa-home" aria-hidden="false"></i>&nbsp;海外地产</p>
        <p class="text">做全球房东,畅享美好生活</p>
        <lubo3></lubo3>
      </div>
    </div>
    <div class="swiper-pagination"></div>
    <!--分页器。如果放置在swiper-container外面，需要自定义样式。-->
  </div>
</template>

<script>
  import Swiper from 'swiper'
  import 'swiper/css/swiper.min.css'
  import lubo1 from '@/components/component/lubo1'
  import lubo2 from '@/components/component/lubo2'
  import lubo3 from '@/components/component/lubo3'

  var i = 0;
  export default {
    name: "pagination",
    components: {
      lubo1,
      lubo2,
      lubo3
    },
    methods: {
    },
    mounted() {
      var mySwiper = new Swiper('.swiper-container', {
        loop: true,
        autoplay: {
          delay: 5000,//5秒切换一次
          disableOnInteraction: false,   //用户点击后不会被中断。
        },
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
          loop: true,
        },
      });
      //鼠标滑过pagination控制swiper切换
      for (i = 0; i < mySwiper.pagination.bullets.length; i++) {
        mySwiper.pagination.bullets[i].onmouseover = function () {
          this.click();
        };
      }
    }
  }


</script>

<style scoped>
  .contents{
    font-weight: bold;
    font-size: 30px;
    margin-left: 20px;
    margin-top: 45px;
  }
  .text{
    font-weight: lighter;
    font-size: 14px;
    margin-left: 20px;
  }
  #bannerSwiper {
    width: 1200px;
    height: 560px;
    overflow: hidden;
  }

  .swiper-container {
    margin-left: auto;
    margin-right: auto;
    position: relative;
    overflow: hidden;
    z-index: 1;
  }

</style>
