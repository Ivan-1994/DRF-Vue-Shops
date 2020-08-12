<template>
    <div v-if="getMyProfileData.user_type === '2'">
        <div v-for="user in getAllUsersP">
            <p class="m-5">
                <router-link class="alert alert-success"
                             :to="{name: 'profile', params: {id: user.id}}">Shop: {{user.email}}
                </router-link>
            </p>
        </div>
    </div>
    <h3 v-else>Don't</h3>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "Users",
        computed: mapGetters(['getAllUsersP', 'getMyProfileData']),
        async mounted() {
            let id = localStorage.getItem('id')
            await this.$store.dispatch("getMyProfile", id)
            await this.$store.dispatch("getAllUsers")
        }
    }
</script>

<style scoped>

</style>
