<template>
  <div class="footer">
    <div class="wrapper">
      <div class="fl">
        <ul>
          <li><a href="">关于链家</a></li>
          <li><a href="">联系我们</a></li>
          <li><a href="">加入我们</a></li>
          <li><a href="">隐私声明</a></li>
          <li><a href="">友情链接</a></li>
        </ul>
      </div>
      <div class="fr">官方客服电话&nbsp;10010&nbsp;9666</div>
      <div class="v1"></div>
    </div>
    <div class="bottom">
      <div class="copyright">
        链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | <i class="fa fa-copyright" aria-hidden="true"></i> Copyright©2010-2019 链家网Lianjia.com版权所有 |
        <br>违法和不良信息举报电话：010-86440676 违法和不良信息举报邮箱：jubaoyouxiang@lianjia.com
      </div>
      <div class="beian">
        <img src="/static/img/beian.png" alt="已备案" style="float: left;width: 18px;height: 18px">
        <p style="float: left;height:20px;color: #888888;font-size: 12px">京公网安备 xxxxxxxxxxxx号</p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "footer"
  }
</script>

<style scoped>
  .footer {
    width: 100%;
    height: 325px;
    background: url('/static/img/bottom.jpg') no-repeat center top;
  }

  /*.wrapper .fl {*/
  /*float: left;*/
  /*}*/
  ul, li {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .v1 {
    height: 62px;
  }

  .fl li {
    float: left;
  }

  .fr {
    float: right;
    color: #7dcfa0;
  }

  .footer .wrapper {
    width: 1195px;
    padding-top: 2px;
    padding-bottom: 10px;
    margin-left: 175px;
    border-bottom: #393939 solid 1px;
    line-height: 75px;

  }

  .fl li a {
    color: #fff;
    margin-right: 25px;
    font-size: 14px;
  }

  .footer .bottom {
    padding-top: 100px;
    padding-left: 175px;
  }
  .copyright {
    color: #888c8e;
    font-size: 12px;
    line-height: 20px;
  }

</style>
