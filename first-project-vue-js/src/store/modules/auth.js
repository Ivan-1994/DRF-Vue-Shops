import Axios from 'axios'
export default ({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {'email': localStorage.getItem('email') || ''},
    id: localStorage.getItem('id')
  },
  mutations: {
  },
  actions: {
    async login({dispatch, commit}, {email, password}) {
      let a = (await Axios.post('http://127.0.0.1:8000/auth/token/login/', {
                email: email, password: password})).data
      localStorage.setItem('token', a['auth_token'])
      localStorage.setItem('email', email)
      Axios.defaults.headers.common['Authorization'] = 'Token ' + a['auth_token']
      let data = (await Axios.get('http://127.0.0.1:8000/auth/users/')).data
      localStorage.setItem('id', data[0].id)
    },
    async register({dispatch, commit}, {email, password}) {
      await Axios.post('http://127.0.0.1:8000/auth/users/', {
        email: email, password: password})
    }
  },
  getters : {
    getUser(state) {
      return state.user
    },
    getUserId(state) {
      return state.id
    },
    checkAuth(state) {
      return state.token ? true : false
    }
  }
})
