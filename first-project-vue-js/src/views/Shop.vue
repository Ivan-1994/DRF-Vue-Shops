<template>
    <div>
        <p>Shop Name: {{getShop.name}}</p>
        <p>Admin ID: {{getShop.user}}</p>
        <p>Connected users ID: {{getShop.connected_users}}</p>
        <div v-if="getMyProfileData.id === getShop.user || getMyProfileData.user_type == 2">
            <h4>Edit:</h4>
            <form class="shopedit" @submit.prevent="shop_edit" style="width: 400px;">
                <div class="form-group">
                <label for="name">Name Shop</label> <br>
                <input required class="form-control" id="name" v-model="name_shop" type="text" placeholder="Name"/> <br>
                </div>
<!--                <p>Delete: Choice Users</p>-->
<!--                <select v-model="selectedUsers" multiple>-->
<!--                    <option v-for="user in getShop.connected_users" v-bind:value="user">{{user}}</option>-->
<!--                </select>-->
<!--                <h3>Choice Users: </h3>-->
<!--                <ul>-->
<!--                    <li v-for="user in selectedUsers">{{user}}</li>-->
<!--                </ul>-->
                <button type="submit" class="btn btn-primary">Edit</button>
            </form>
        </div>
    </div>
</template>

<script>

    import {mapGetters} from "vuex";

    export default {
        name: "Shop",
        props: ['id'],
        computed: mapGetters(['getShop', 'getMyProfileData']),
        data() {
            return {
                selectedUsers: [],
                name_shop: ''
            }
        },
        async mounted() {
            let id = this.$route.params.id
            await this.$store.dispatch("getMyProfile")
            await this.$store.dispatch("Shop", id)
        },
        methods: {
            shop_edit: function () {
                let name = this.name_shop
                let users = this.selectedUsers
                let id = this.id
                this.$store.dispatch('editShop', {name, id})
                    // .then(() => this.$router.push('/'))
                    .catch(err => console.log(err))
            }
        }
    }
</script>

<style scoped>

</style>
