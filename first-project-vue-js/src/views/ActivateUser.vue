<template>
    <div>
        <h3>Email Activate</h3>
    </div>
</template>

<script>

    export default {
        name: "ActivateUser",
        async mounted() {
            let id = this.$route.params.id
            let uuid = this.$route.params.uuid
            if (id && uuid) {
                await this.$store.dispatch("getActivateUser", {id, uuid})
            } else {
                this.$router.push('/')
            }
        }
    }
</script>

<style scoped>

</style>
