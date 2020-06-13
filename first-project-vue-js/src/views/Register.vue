<template>
  <div v-if="!getUserProfile.id">
    <h5>Sign-up</h5>
    <form @submit.prevent="register" style="width: 400px">
<!--      <label for="name">Name</label>-->
<!--      <div>-->
<!--          <input id="name" type="text" v-model="name" required autofocus>-->
<!--      </div>-->
        <div class="form-group">
      <label for="email" >E-Mail Address</label>

          <input class="form-control" id="email" type="email" v-model="email" required>
      </div>

    <div class="form-group">
      <label for="password">Password</label>

          <input class="form-control" id="password" type="password" v-model="password" required>
      </div>

<!--      <label for="password-confirm">Confirm Password</label>-->
<!--      <div>-->
<!--          <input id="password-confirm" type="password" v-model="password_confirmation" required>-->
<!--      </div>-->

      <div>
          <button type="submit" class="btn btn-primary">Sign-up</button>
      </div>
    </form>
  </div>
    <h3 v-else>Don't</h3>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
      name: 'register',
      computed: mapGetters(['getUserProfile']),
      async mounted() {
            await this.$store.dispatch("getProfile")
        },
      data: () => ({
        // name : "",
        email : "",
        password : "",
        // password_confirmation : ""
      }),
      methods: {
      register: function () {
        let data = {
          // name: this.name,
          email: this.email,
          password: this.password
        }
        this.$store.dispatch('register', data)
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
    }
  }
</script>
