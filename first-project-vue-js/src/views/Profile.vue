<template>
    <div v-if="getUserProfile.id">
        <p>Последний вход: {{getUserProfile.last_login}}</p>
        <p>Эмейл: {{getUserProfile.email}}</p>
        <p>Имя: {{getUserProfile.first_name}}</p>
        <p>Фамилия: {{getUserProfile.last_name}}</p>
        <form class="profile" @submit.prevent="profile" style="width: 400px;">
            <h4>Edite</h4>
            <div class="form-group">
            <label for="first_name">First Name</label>
            <input class="form-control" id="first_name" v-model="first_name" type="text" placeholder="FirstName"/>
            </div>
            <div class="form-group">
            <label for="last_name">Last Name</label>
            <input class="form-control" id="last_name" v-model="last_name" type="text" placeholder="LastName"/>
            </div>
                <div class="form-group">
            <label for="email">Email</label>
            <input class="form-control" id="email" v-model="email" type="email" placeholder="Name"/>
                </div>
                    <div class="form-group">
            <label for="password">Password</label>
            <input class="form-control" id="password" v-model="password" type="password" placeholder="Password"/>
                    </div>
            <button type="submit" class="btn btn-primary">Edit</button>
        </form>
    </div>
    <h3 v-else>Don't</h3>
</template>

<script>
    import {mapGetters} from "vuex";
    export default {
        name: "profile",
        computed: mapGetters(['getUserProfile']),
        async mounted() {
            let id = this.$route.params.id
            await this.$store.dispatch("getProfile", id)
        },
        data() {
            return {
                first_name: "",
                last_name: "",
                email: "",
                password: ""
            }
        },
        methods: {
            profile: function () {
                let first_name = this.first_name
                let last_name = this.last_name
                let email = this.email
                let password = this.password
                let id = this.$route.params.id
                this.$store.dispatch('editProfile', {first_name, last_name, email, password, id})
                    .then(() => window.location.reload())
                    .catch(err => console.log(err))
            }
        }
    }

</script>

<style scoped>

</style>
