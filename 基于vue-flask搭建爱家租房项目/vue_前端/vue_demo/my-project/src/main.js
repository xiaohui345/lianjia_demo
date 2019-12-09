// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import store from'./store/store'
// import 'bootstrap'


Vue.config.productionTip = false;

//在vue的全局变量中设置了$axios = axios
Vue.prototype.$axios = axios;
// 以后在每个组件中使用时： this.$axios



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
