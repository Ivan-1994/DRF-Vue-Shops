import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import Axios from "axios";

const token = localStorage.getItem('token')
if (token) {
    Axios.defaults.headers.common['Authorization'] = 'Token ' + token
}

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
