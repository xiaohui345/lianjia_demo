import vuex from 'vuex'
import Vue from 'vue'
import vuecookies from 'vue-cookies'


Vue.use(vuex);
Vue.use(vuecookies);


export default new vuex.Store({
  state: {
    username: vuecookies.get('username'),
    token: vuecookies.get('token'),
    //存放的数据可以供全局使用；
    apilist: {
      login: 'http://127.0.0.1:5000/login',
      register: 'http://127.0.0.1:5000/register'
    },
    house_data:vuecookies.get('house_data'),
    city:vuecookies.get('city')
  },
  mutations: {
    //这里存的数据是暂时的，一刷新后就消失了，因此必须把数据保存到cookies里面去。
    changeuser(state, data) {
      //页面不刷新
      state.username = data.username;
      state.token = data.token;
      //当刷新页面的时候就到cookies中取值
      vuecookies.set('username', data.username, '20min');
      vuecookies.set('token', data.token, '20min')
    },
    deleteUser(state) {
      //删除的话也要删除cookies里面
      state.username = '';
      state.token = '';
      vuecookies.remove("username");
      vuecookies.remove("token")
    },
    putdata(state,data) {
      //把后端传入过来的数据放入到cookies中
      state.house_data = data;
      vuecookies.set('house_data', data, '2day');
    },
    city(state,data) {
      //把后端传入过来的数据放入到cookies中
      state.city = data;
      vuecookies.set('city', data, '2day');
    }
  },
  actions: {
    changeuser(context, data) {
      context.commit('changeuser', data)
    },
    deleteUser(context){
      context.commit('deleteUser')
    },
    putdata(context,data){
      context.commit('putdata',data)
    },
    city(context,data){
      context.commit('city',data)
    }
  }
})

