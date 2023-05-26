<template>
  <body>
    <nav >
      <div class="mobile-menu-toggle" @click="toggleMobileMenu">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
      <div class="menu-links" :class="{ 'mobile-menu-open': isMobileMenuOpen }">
        <router-link to="/" :class="{ 'custom-link-active': $route.path === '/' }">Login</router-link> |
        <router-link to="/Services" :class="{ 'custom-link-active': $route.path === '/Services' }">Services</router-link> |
        <router-link to="/Registration" :class="{ 'custom-link-active': $route.path === '/Registration' }">Registration</router-link> |
        <router-link to="/Unregister" :class="{ 'custom-link-active': $route.path === '/Unregister' }">Unregistration</router-link> |
        <router-link to="/Employeeregis" :class="{ 'custom-link-active': $route.path === '/Employeeregis' }">New Employee Registration</router-link> |
        <router-link to="/edit_seecars" :class="{ 'custom-link-active': $route.path === '/edit_seecars' }">Edit & View Cars</router-link>
      </div>
  </nav>
  <div class="contain">
    <h3 class="card-title mb-0" style="color:white;">Employee Registration</h3>
          <!-- </div> -->
          <!-- <div class="card-body"> -->
            <br>
            <div v-if="showSuccessMessage" class="alert alert-success mt-3" role="alert">
              Employee registered!
            </div>
            <form>
              <!-- <div class="mb-3"> -->
                <label for="username" class="form-label" style="color: aliceblue;">Email</label>
                <input type="email" class="form-control" placeholder="Enter  Email" required v-model="this.a_email">
              <!-- </div> -->
              <!-- <div class="mb-3"> -->
                <br>
                <label for="password" class="form-label" style="color: aliceblue;">Password</label>
                <input type="password" class="form-control" placeholder="Set Password" required v-model="this.a_pass">
              <!-- </div> -->
              <!-- <div class="mb-3"> -->
                <br>
              <!-- </div> -->
              <div class="mb-3 d-grid gap-2">
                <button type="button" class="btn btn-primary" @click="handleSubmit">Submit</button>
                <button type="reset" class="btn btn-secondary">Reset</button>
              </div>
            </form>
  </div>
  </body>

</template>

<script>
import { getAPI } from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/axios-api.js'
import axios from 'axios';
import router from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/src/router'

export default {
    name: 'Employeeregis',
    data(){
    return {
    APIData:[],
    CheckData:[],
    a_email:'',
    a_pass:'',
    showlogin:true,
    // tempLoggedIn:false,
    isLoggedIn:false,
    passnotcorrect:false,
    admininfonotthere:false,
    showSuccessMessage:false,
    isMobileMenuOpen: false
  }
},
methods :{
      handleSubmit(event){
      event.preventDefault();
      const confirmed = window.confirm("Are You Sure You want to Register a new employee")
      if (confirmed){
      axios.get(`http://127.0.0.1:8000/adminaccess/`,)
      .then(response => {
          console.log('asking all admin info');
          // Handle the response
          this.CheckData = response.data;
          console.log("here");
          console.log(this.CheckData);
          
          const targetValue = this.a_email;
          const regularArray = [...this.CheckData];
          const isValuePresent = regularArray.some(item => item.Email === targetValue);

          if (isValuePresent){
            console.log("already there");
            this.resetData();
          }
          else{
            axios.post(`http://127.0.0.1:8000/adminaccess/${this.a_email}/`, {
            Email: this.a_email,
            Password: this.a_pass
              })
           .then(response => {
            console.log('Registered');
            // Handle the response
            this.showSuccessMessage=true;
              // localStorage.setItem('isLoggedIn', false);
              setTimeout(() => {
              this.resetData();
                }, 2000);
              
                            })         }   })      }
      else {
            setTimeout(() => {
              this.$router.push('/Employeeregis');
              this.resetData();
                }, 2000);
              }
        //   .catch(error => {
        //   console.error('Admin info is not there');
        //   this.showlogin=false;
        //   this.admininfonotthere=true;
        //   setTimeout(() => {
        //     this.$router.push('/');
        //     this.resetData();
        //       }, 2000);
        // });

        },

    toggleMobileMenu() {
    this.isMobileMenuOpen = !this.isMobileMenuOpen;
      },
    resetData(){
      this.APIData=[],
      this.a_email='',
      this.a_pass='',
      this.showlogin=true,
      // this.tempLoggedIn=false,
      this.passnotcorrect=false,
      this.admininfonotthere=false,
      this.showSuccessMessage=false
    }
  }
}
</script>

<style>
  .contain{
    margin-top: 100px;
    backdrop-filter: blur(20px);
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
    padding: 30px;
  }

  @media only screen and (max-width: 600px) {
    .menu-links {
    display: none;
  }

  .mobile-menu-toggle {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 30px;
    height: 20px;
    cursor: pointer;
  }

  .bar {
    width: 100%;
    height: 2px;
    background-color: white;
  }

  .mobile-menu-open {
    display: block;
  }
  }
</style>