<template>
  <div>
    <div class="c1">
      <Vheader></Vheader>
      <span class="exchange"><i></i><router-link to="/city" tag="span">
        <span v-if="cityname">{{cityname}}</span>
        <span v-else>北京</span>
      </router-link></span>
      <h2 style="text-align: center;font-size: 55px;font-weight: bold;color: white;padding-top: 50px">连接每个家庭的故事</h2>
    </div>
    <div class="home-nav">
      <ul class="count-3">
        <li class="hvr-bob CLICKDATA" data-click-evtid="20600" data-click-event="WebClick"
            data-action="click_name=找二手房"><a href="/ershoufang/"><img
          src="/static/img/house.png"><b>找二手房</b>
          <p>真实二手房源，链家承诺真实在售 所见即真</p></a></li>
        <li class="hvr-bob CLICKDATA" data-click-evtid="20600" data-click-event="WebClick"
            data-action="click_name=房屋估价"><a href="yezhu/gujia/"><img
          src="/static/img/phphnmv10.png"><b>房屋估价</b>
          <p>基于海量成交数据，帮您合理定价预估市值</p></a></li>
        <li class="hvr-bob CLICKDATA" data-click-evtid="20600" data-click-event="WebClick"
            data-action="click_name=地图找房"><a href="/ditu/"><img
          src="/static/img/postion.png"><b>地图找房</b>
          <p>为您精准定位，位置周边配置一览无余</p></a></li>
      </ul>
    </div>
    <div class="hand-lianjia">
      <div class="wrapper">
        <div class="fl">
          <div class="titles"><span style="font-size: 35px">一链倾城</span>
            <h2 style="font-size: 50px;font-weight: bold">为你为全家</h2></div>
          <p>集二手、新房、租房功能于一体，随时随地任性找房。IM匿名咨询让您放心，消息动态推送让您省心，服务承诺让您安心，数据百科锦囊让您感受贴心漫漫找房路，我们努力为您想更多。</p>
          <div class="download">
            <div class="hand-app"><a href="https://itunes.apple.com/cn/app/id405882753?mt=8" class="ios" target="_blank"
                                     rel="nofollow"></a><a
              href="https://m.lianjia.com/download/lianjia?utm_source=_lianjia_zhilian_pc&amp;utm_medium=&amp;platform=pc&amp;cid="
              class="android" rel="nofollow"></a></div>
            <div class="erweima" style="background: none;"><img style="width: 120px;"
                                                                src="//ajax.api.lianjia.com/qr/getDownloadQr?location=site_middle&amp;ljweb_channel_key=site_index">
            </div>
          </div>
        </div>
      </div>
    </div>
    <Pagination></Pagination>
    <Footer></Footer>
  </div>

</template>

<script>
  import Vheader from '@/components/Vheader'
  import Pagination from '@/components/component/pagination'
  import Footer from '@/components/component/footer'

  export default {
    name: "Vmain",
    data() {
      return {
        cityname:this.$store.state.city
      }
    },
    components: {
      Vheader,
      Pagination,
      Footer
    },
    created(){

    },
    methods: {},
    computed: {},
    mounted() {
      var that = this;
      this.$axios.request({
        url: 'http://127.0.0.1:5000/house',
        method: 'get',
      }).then(function (arg) {
        if (arg.data.code === 1000) {
          console.log("data", arg.data.data, typeof arg.data.data);
          // console.log("data",arg.data.data.newhouse,typeof arg.data.data.newhouse);
          that.$store.dispatch('putdata', arg.data.data);
        }
      })
    }
  }
</script>

<style scoped>
  .home-nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: block;
  }

  .home-nav ul.count-3 li {
    width: 33%;
  }

  .home-nav li {
    float: left;
  }

  .home-nav li img {
    width: 76px;
    height: 65px;
    margin: 35px auto 17px auto;
    display: block;
    vertical-align: middle;
  }

  .home-nav li b {
    font-size: 18px;
    color: #394043;
    font-weight: 400;
    font-style: normal;
    padding-left: 215px;
  }

  .home-nav li p {
    width: 183px;
    margin: 3px auto 5px auto;
    font-size: 12px;
    color: #b0b3b4;
    line-height: 20px;
    padding-left: 25px;
  }

  li {
    list-style: none;
    margin: 0;
    padding: 0;
    display: list-item;
    text-align: -webkit-match-parent;
  }

  .c1 {
    height: 500px;
    background: url("/static/img/bannerV2.jpg") center top;
    background-attachment: fixed; /*把背景图固定*/
  }

  .home-nav {
    height: 250px;
    background-color: white;
  }

  .hand-lianjia {
    padding-top: 45px;
    background: url('/static/img/bg-app.jpg') center top;
    height: 500px;
  }

  .hand-lianjia .fl {
    margin-left: 65px;
  }

  .hand-lianjia .fl .titles {
    background-position: -448px -379px;
    width: 450px;
    height: 118px;
  }

  .hand-lianjia .fl .titles h2 {
    margin-top: 5px;
  }

  .hand-lianjia .fl p {
    width: 450px;
    height: 118px;
    line-height: 22px;
    margin-top: 22px;
  }

  .wrapper {
    width: 150px;
    padding-left: 120px;
  }

  .c1 .exchange {
    background: rgba(0, 0, 0, 0.25);
    display: inline-block;
    height: 36px;
    line-height: 27px;
    text-align: center;
    color: #fff;
    margin-top: 20px;
    margin-left: 35px;
    cursor: pointer;
    border-radius: 25px;
    padding: 4px 10px;
    font-size: 15px;
  }

  .c1 .exchange i {
    background-image: -webkit-image-set(url('/static/img/spriteV2_new.png') 1x, url('/static/img/spriteV2_new@2x.png') 2x);
    background-position: -189px -20px;
    width: 10px;
    height: 12px;
    display: inline-block;
    position: relative;
    margin-right: 6px;
    top: 1px;
  }
</style>
