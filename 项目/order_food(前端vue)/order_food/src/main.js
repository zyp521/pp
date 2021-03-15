// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import Vuex from 'vuex'
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Vuex)
const store=new Vuex.Store({
   state:{
      count_food:0,
      sum_price:0
   },
   mutations:{
      incre(state,myprice){
        state.count_food+=1
        state.sum_price+=myprice.price
      }
   },
  actions:{
      increment(context,goodsprice){
        context.commit("incre",goodsprice)
      }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
