<template>
  <div>
    <link rel="stylesheet" href="/static/css/fontastic.css">
    <link rel="stylesheet" href="/static/css/style.default.css" id="theme-stylesheet">
    <link rel="stylesheet" href="/static/css/custom.css">
    <div class="page login-page">
      <div class="container d-flex align-items-center">
        <div class="form-holder has-shadow">
          <div class="row">
            <!-- Logo & Information Panel-->
            <div class="col-lg-6 imgput">
              <div class="d-flex align-items-center">
                <div class="content">
                  <div class="logo">
                    <h1 style="font-size: 40px;font-weight: 700;padding-left: 100px">链家网</h1>
                  </div>
                  <p style="font-size: 30px;padding-left: 100px">链接每个家庭的故事</p>
                </div>
              </div>
            </div>
            <!-- Form Panel    -->
            <div class="col-lg-6">
              <div class="content">
                <div class="form-group">
                  <label class="label-materi font-login">User Name</label>
                  <input type="text" placeholder="输入用户名" class="form-control" v-model="username" style="width: 300px">
                  <p class="error"></p>
                </div>
                <div class="form-group">
                  <label class="label-material font-login">password</label>
                  <input type="password" placeholder="输入密码" class="form-control" v-model="password"
                         style="width: 300px">
                  <p class="error"></p>
                </div>
                <div class="form-group">
                  <button id="regidter" type="submit" name="registerSubmit" class="btn btn-primary font-login"
                          @click="loginclick">
                    Login
                  </button>
                  <!--@click -- v-on:click -->
                </div>
                <h4 style="font-size: 15px">Already have an account?</h4>
                <a href="/register" class="signup" style="font-size: 15px">Register</a>
                <p style="color: red"></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

  export default {
    name: "login",
    data() {
      return {
        username: '',
        password: '',
        oldUrl:''
      }
    },
    //beforeRouteEnter在mounted之后执行；
    beforeRouteEnter(to,from,next){
      next(vm =>{
      // 通过访问vm来访问组件的实例;vm--->this
        console.log(vm);
        //from表示从哪个路由来的from.path是上一个Url的路径
        //vm.oldUrl也是上一个Url的路径
        console.log(from);
        vm.oldUrl = from.path
      })
    },
    methods: {

      // this.$axios.request里面的this和外面的this不是一致的；

      loginclick() {

        var that = this;

        this.$axios.request({
          //that.$store 只是没有提示而已
          url: that.$store.state.apilist.login,
          method: 'post',
          data: {
            username: that.username,
            password: that.password
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(function (arg) {
          //执行成功后返回该回调函数
          //  arg.data为返回的结果
          if (arg.data.code === 1000) {
            // //把返回的数据保存到store里面，方便全局调用
            // that.$store.state.nickname = arg.data.data.nickname;
            //通过分发action来调用对应的mutation里面的方法进而修改state里面的值
            console.log(arg.data.data);
            that.$store.dispatch('changeuser',arg.data.data);
            //拿到返回登录之前的url
            var tourl = that.oldUrl;
            if (tourl) {
              that.$router.push({  //重定向
                path: tourl
              })
            } else {
              that.$router.push({
                path: '/'
              })
            }
          } else {
            alert(arg.data.error)
          }
        }).catch(function (arg) {
          console.log(arg)
        })
      }
    }
  }

</script>

<style scoped>
  .error {
    color: red !important;
  }

  .imgput {
    background: url("/static/img/bannerV2.jpg");
    height: 500px;
  }

  .content {
    margin-top: 150px;
    margin-left: 100px;
  }

  .font-login {
    font-weight: bolder;
    font-size: 15px
  }
</style>
