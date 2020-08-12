<template>
    <div v-if="getUserProfile.id">
        <form @submit.prevent="createShop" style="width: 400px">
            <h5>Create Shop</h5>
            <div class="form-group">
                <label for="name">Name Shop</label>
                <input required class="form-control" v-model="name" type="text" placeholder="Name Shop" id="name"/>
            </div>
            <button type="submit" class="btn btn-primary">Create</button>

        </form>
    </div>
    <h3 v-else>Don't</h3>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "CreateShop",
        computed: mapGetters(['getUserProfile']),
        async mounted() {
            let id = localStorage.getItem('id')
            await this.$store.dispatch("getProfile", id)
        },
        data() {
            return {
                name: ""
            }
        },
        methods: {
            createShop: function () {
                let name = this.name
                this.$store.dispatch('createShop', {name})
                    .then(() => {
                        this.$router.push('/')
                        window.location.reload()
                    })
                    .catch(err => console.log(err))
            }
        }
    }
</script>

<style scoped>

</style>
