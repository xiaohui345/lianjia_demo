import Vue from 'vue'
import Router from 'vue-router'
import Vmain from '@/components/Vmain'
import login from '@/components/login'
import register from '@/components/register'
import ershoufang from '@/components/ershoufang'
import xinfang from '@/components/xinfang'
import city from '@/components/component/city'

Vue.use(Router);

export default new Router({
  // mode: 'history', //去除路由地址中的#
  routes: [
    {
      path: '/',
      name: 'Vmain',
      component: Vmain,
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
    {
      path: '/register',
      name: 'register',
      component: register,
    },
    {
      path: '/ershoufang',
      name: 'ershoufang',
      component: ershoufang,
    },
    {
      path: '/xinfang',
      name: 'xinfang',
      component: xinfang,
    },
      {
      path: '/city',
      name: 'city',
      component: city,
    },
  ]
})
