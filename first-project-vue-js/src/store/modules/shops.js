import Axios from 'axios'

export default {
    state: {
        shops: [],
        shopData: {}
    },
    mutations: {
        updateShops(state, shops) {
            state.shops = shops
        },
        updateShop(state, shopData) {
            state.shopData = shopData
        }
    },
    actions: {
        async fetchShops(ctx) {
            // let a = (await Axios.post('http://127.0.0.1:8000/auth/token/login/', {
            //     email: 'ivan.ponomarenko94@gmail.com', password: 'qazwsxedc'})).data
            // localStorage.setItem('token', a['auth_token'])
            //

            // console.log((await Axios.get('http://127.0.0.1:8000/users/')).data);
            // console.log((await Axios.get('http://127.0.0.1:8000/shops/')).data);
            // console.log((await Axios.post('http://127.0.0.1:8000/auth/users/', {
            //     email: 'ivan.ponomarenk@gmail.com', password: 'qazwsxedc21'})));  // Sign-up

            // console.log((await Axios.post('http://127.0.0.1:8000/auth/token/login/', {
            //     email: 'ivan.ponomarenko94@gmail.com', password: 'qazwsxedc'})));  // Token
            // console.log(Axios.defaults)

            const shops = (await Axios.get("http://127.0.0.1:8000/shops/")).data;
            ctx.commit('updateShops', shops)
        },
        async Shop({dispatch, commit}, id) {
            let shopData = (await Axios.get('http://127.0.0.1:8000/shop/' + id)).data;
            commit('updateShop', shopData)
        },
        async editShop({dispatch, commit}, {name, id}) {
            let data = {}
            if (name){
                data['name'] = name
            }
            // if (users) {
            //     data['connected_users'] = users
            // }
            await Axios.put('http://127.0.0.1:8000/shop/' + id, data)
            .catch(err => console.log(err));
        },
        async createShop({dispatch, commit}, {name}) {
            let data = {}
            if (name){
                data['name'] = name
            }
            await Axios.post('http://127.0.0.1:8000/shops/', data)
            .catch(err => console.log(err));
        },
        async putSubscribeShop({dispatch, commit}, {id}) {
            let myId = localStorage.getItem('id')
            await Axios.put('http://127.0.0.1:8000/shop/' + id, {'connected_users': [myId]})
            .catch(err => console.log(err));
        }

    },
    getters: {
        allShops(state) {
            return state.shops
        },
        getShop(state) {
            return state.shopData
        }
    },
}
