<template>
    <div id="app">
        <!--        <div id="nav">-->
        <!--            <router-link to="/">Shops</router-link>-->
        <!--            |-->
        <!--            <span v-if="!checkAuth"><router-link to="/login">login</router-link> |</span>-->
        <!--            <router-link v-if="!checkAuth" to="/register">register</router-link>-->
        <!--            <router-link v-if="checkAuth" to="/profile">profile</router-link>-->
        <!--        </div>-->

        <nav class="navbar navbar-expand navbar-light bg-light">
            <router-link class="navbar-brand" to="/">Shops</router-link>

            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li v-if="!checkAuth" class="nav-item">
                        <router-link class="nav-link" to="/login">Sign-in</router-link>
                    </li>
                    <li v-if="!checkAuth" class="nav-item">
                        <router-link class="nav-link" to="/register">Sign-up</router-link>
                    </li>
                    <li class="nav-item" v-if="checkAuth">
                        <router-link class="nav-link" :to="{name: 'profile', params: {id: getMyProfileData.id}}">Profile</router-link>
                    </li>
                    <li class="nav-item" v-if="checkAuth">
                        <router-link class="nav-link" to="/shop/create">Create Shop</router-link>
                    </li>
                    <li class="nav-item" v-if="getMyProfileData.user_type === '2'">
                        <router-link class="nav-link" to="/users">Users</router-link>
                    </li>
                </ul>
                <h6 v-if="getMyProfileData.email">{{getMyProfileData.email}}</h6>
            </div>
        </nav>
        <div class="container-fluid">
        <router-view/>
            </div>
    </div>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: 'App',
        computed: mapGetters(['getUser', 'checkAuth', 'getMyProfileData']),
        async mounted() {
            let id = localStorage.getItem('id')
            await this.$store.dispatch("getMyProfile", id)
        },
    }
</script>

<style lang="scss">
</style>
