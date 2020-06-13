import Axios from 'axios'

export default {
    state: {
        userProfile: {},
        allUsers: {},
        myProfile: {}
    },
    mutations: {
        updateUserProfile(state, userProfile) {
            state.userProfile = userProfile
        },
        updateMyProfile(state, myProfile) {
            state.myProfile = myProfile
        },
        updateAllUser(state, allUsers) {
            state.allUsers = allUsers
        }
    },
    actions: {
        async editProfile({dispatch, commit}, {first_name, last_name, email, password, id}) {
            console.log(id)
            let mass = [first_name, last_name, email, password]
            let massKey = ['first_name', 'last_name', 'email', 'password']
            let data = {}
            for (let i = 0; i < 4; i++) {
              if (mass[i]) {
                  data[massKey[i]] = mass[i]
              }
            }
            console.log((await Axios.get('http://127.0.0.1:8000/user/' + id)).data, data)
            await Axios.put('http://127.0.0.1:8000/user/' + id, data)
        },
        async getProfile({dispatch, commit}, id) {
            if (id) {
                const userProfile = (await Axios.get('http://127.0.0.1:8000/user/' + id)).data;
                commit('updateUserProfile', userProfile)
            }
        },
        async getMyProfile({dispatch, commit}, id) {
            if (id) {
                const myProfile = (await Axios.get('http://127.0.0.1:8000/user/' + id)).data;
                commit('updateMyProfile', myProfile)
            }
        },
        async getAllUsers(ctx) {
            const allUsers = (await Axios.get('http://127.0.0.1:8000/users/')).data;
            ctx.commit('updateAllUser', allUsers)
        },
    },
    getters: {
        getUserProfile(state) {
            return state.userProfile
        },
        getAllUsersP(state) {
            return state.allUsers
        },
        getMyProfileData(state) {
            return state.myProfile
        }

    },
}
