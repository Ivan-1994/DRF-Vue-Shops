import Vue from 'vue'
import Vuex from 'vuex'
import shops from "./modules/shops";
import auth from "./modules/auth";
import users from "./modules/users";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    shops,
    auth,
    users
  }
})
