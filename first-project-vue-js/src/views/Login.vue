<template>
 <div v-if="!getUserProfile.id">
   <form class="login" @submit.prevent="login" style="width: 400px">
     <h5>Sign-in</h5>
     <div class="form-group">
     <label for="InputEmail" >Email</label>
     <input required class="form-control" v-model="email" type="email" placeholder="Email" id="InputEmail"/>
     </div>
     <div class="form-group">
       <label for="InputPass">Password</label>
     <input required class="form-control" v-model="password" type="password" placeholder="Password" id="InputPass"/>
    </div>
     <button type="submit" class="btn btn-primary">Sign-in</button>

   </form>
 </div>
    <h3 v-else>Don't</h3>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
    computed: mapGetters(['getUserProfile']),
    async mounted() {
            await this.$store.dispatch("getProfile")
        },
    data(){
      return {
        email : "",
        password : ""
      }
    },
    methods: {
      login: function () {
        let email = this.email
        let password = this.password
        this.$store.dispatch('login', { email, password })
       .then(() => {
         this.$router.push('/')
         window.location.reload()
       })
       .catch(err => console.log(err))
      }
    }
  }
</script>
