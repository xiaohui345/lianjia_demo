<template>
  <nav class="navbar navbar-default">
    <div class="container-fluid">
      <div class="navbar-header">
        <!--<img src="/static/img/favicon.ico" width="55" height="50" onload="resizeImage(this)" alt="链家">-->
        <a class="logo"></a>
      </div>
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li v-for="(item,index) in routes" :class="{active:index===currentIndex}" @click="activeHander(index)">
            <router-link :to="item.url">{{item.title}}</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <!--需要判断用户是否是登录状态-->
          <li v-if="this.$store.state.username">
            <!--如果用户登录了就把他的昵称替换登录-->
            <a>{{this.$store.state.username}}</a>
          </li>
          <li v-else>
            <router-link to="/login">
              <span>
                <i class="fa fa-user-circle fa-1x" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;登录
              </span>
            </router-link>
          </li>
          <li v-if="this.$store.state.username">
            <a @click="loginout"><span>注销</span></a>
          </li>
          <li v-else>
            <router-link to="/register"><span>注册</span></router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: "Vheader",
    data() {
      return {
        routes: [
          {url: "/", title: "首页"},
          {url: "/ershoufang", title: "二手房"},
          {url: "/xinfang", title: '新房'},
          {url: "/zufang", title: '租房'},
          {url: "/fangjia", title: '房价'},
          {url: "/zhinan", title: '指南'},
        ],
        currentIndex: null,
      }
    },
    methods: {
      activeHander(index) {
        this.currentIndex = index
      },
      loginout(){
        this.$store.dispatch('deleteUser')
      }
    }
  }

</script>

<style scoped>
  * {
    padding: 0;
    margin: 0;
  }

  .logo {
    display: inline-block;
    /*根据一系列的图片,然后根据位置坐标来确定其中的一个图片,这样可以节省很多的空间。*/
    background-image: url('/static/img/sprite.png');
    background-position: -120px -284px;
    height: 32px;
    vertical-align: middle;
    width: 125px;
    padding-left: 2px;
    margin-top: 5px;
  }

  .navbar {
    /*0消除圆角;非0 生成导航条圆角*/
    border-radius: 0
  }

  body {
    font-size: 14px;
    color: white;
  }

  ul {
    list-style: none;
  }

  a {
    text-decoration: none;
  }

  .navbar {
    background-color: white;
  }
</style>
