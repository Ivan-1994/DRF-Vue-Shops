<template>
  <div class="home">
    <h4>Shops: {{allShops.length}}</h4>
    <br>
    <div v-for="shop in allShops">
      <p class="m-5"><router-link class="alert alert-success" :to="{name: 'shop', params: {id: shop.shop_id}}">Shop: {{shop.name}}</router-link></p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import {mapGetters} from "vuex"
export default {
  name: 'Home',
  computed: mapGetters(['allShops']),
  async mounted() {
    await this.$store.dispatch("fetchShops")
  }
}
</script>
