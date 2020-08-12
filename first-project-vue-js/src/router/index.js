import Vue from 'vue'
import VueRouter from 'vue-router'
import Shops from '../views/Shops.vue'
import Shop from "../views/Shop";
import Login from '../views/Login.vue'
import Secure from '../components/Secure.vue'
import Register from '../views/Register.vue'
import Profile from "../views/Profile";
import CreateShop from "../views/CreateShop";
import Users from "../views/Users";
import ActivateUser from "../views/ActivateUser";

Vue.use(VueRouter);

  const routes = [
  {
    path: '/',
    name: 'Shops',
    component: Shops
  },
  {
    path: '/shop/create',
    name: 'CreateShop',
    component: CreateShop
  },
  {
    path: '/shop/:id',
    name: 'shop',
    component: Shop,
    props: true
  },
  {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: Profile
    },
      {
      path: '/activate_email/:id/:uuid',
      name: 'ActivateUser',
      component: ActivateUser
    },
      {
      path: '/users',
      name: 'Users',
      component: Users
    },
    {
      path: '/secure',
      name: 'secure',
      component: Secure,
      meta: {
        requiresAuth: true
      }
    },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
