<template>
  <body>
    <div v-if="showlogin">
        <div class="content">
          <!-- <br> -->
          <h2 style="color: white;">Cogniver</h2><br>
          <h2 style="color: white;"><i class="bx bx1-firebase"></i>Valet Parking Software</h2><br>
          <!-- <div class="text-sci" style="color: white;"> -->
          <h2>Welcome!</h2>
          <br>
          <!-- </div> -->
        </div>
        <!-- <div class="loginn"> -->
          <div class="form-container">
            <form>
              <h2 class="text-center mb-4" style="color: aliceblue;">Employee Login</h2>
              <div class="mb-3">
                <label for="username" class="form-label" style="color: aliceblue;">Email</label>
                <input type="email" class="form-control" placeholder="Enter Registered Email" required v-model="adminemail">
              </div>
              <div class="mb-3">
                <label for="password" class="form-label" style="color: aliceblue;">Password</label>
                <input type="password" class="form-control" placeholder="Password" required v-model="adminpass">
              </div>
              <button type="button" class="btn btn-primary" @keyup.enter="checklogin" @click="checklogin" >Login</button>
            </form>
          </div>
        <!-- </div> -->
      
    </div>
    <div v-if="passnotcorrect" class="alert alert-danger mt-3" role="alert">
       Password not correct!
    </div>
    <div v-if="admininfonotthere" class="alert alert-danger mt-3" role="alert">
       Invalid Admin email is not registered!
    </div>
  </body>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { getAPI } from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/axios-api.js'
import axios from 'axios';
import router from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/src/router'
export default {
  name: 'Home',
  components: {
  },
  data(){
    return {
    APIData:[],
    adminemail:'',
    adminpass:'',
    showlogin:true,
    // tempLoggedIn:false,
    isLoggedIn:false,
    passnotcorrect:false,
    admininfonotthere:false,
    showSuccessMessage:false
  }
  },
  mounted(){
    // const tempLoggedIn=false
    localStorage.setItem('isLoggedIn', false)
    // if (this.tempLoggedIn=="false"){
    //   localStorage.setItem('isLoggedIn', false);
    // }
  },
  methods :{
    checklogin(event){
    event.preventDefault();
    const aemail = this.adminemail;
    const apass=this.adminpass;

      axios.get(`http://127.0.0.1:8000/adminaccess/${aemail}/`,)
      .then(response => {
          console.log('Admin info is ttthere');
          // Handle the response
          this.APIData = response.data;
          console.log(this.APIData);
          if (apass==this.APIData.Password){
            console.log("correct pppass");
            // Set flag in local storage to indicate successful login
            localStorage.setItem('isLoggedIn', true);
            // this.isLoggedIn = true;
            router.push({ name: 'Services' });
            // localStorage.setItem('isLoggedIn', false);
            this.resetData();
            // setTimeout(() => {
            // this.resetData();
            //   }, 2000);
            
          }
          else {
          console.error('Password not correct');
          this.showlogin=false;
          this.passnotcorrect=true;
          setTimeout(() => {
            this.$router.push('/');
            this.resetData();
              }, 2000);
          }
        })
      .catch(error => {
          console.error('Admin info is not there');
          this.showlogin=false;
          this.admininfonotthere=true;
          setTimeout(() => {
            this.$router.push('/');
            this.resetData();
              }, 2000);
        });
    },
    resetData(){
      this.APIData=[],
      this.adminemail='',
      this.adminpass='',
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
  body {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 100vh;
    background: url('/Users/gauravrastogi/Desktop/valet_parking_vue/valet/cosmic-2.jpg') no-repeat;
    background-size: cover;
    background-position: center;
  }


   .content {
    /* width: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: auto;
    background: transparent;
    padding-top: 40px; 
    color: #e4e4e4; */
    width: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: auto;
  background: transparent;
  padding-top: 10px; 
  color: #e4e4e4;
  }

  .text-sci h2 {
    font-size: 24px;
    line-height: 1;
    margin-top: 0;
  }

  .text-sci h2 span {
    font-size: 18px;
  }

  .text-sci p {
    font-size: 14px;
    margin: 20px 0;
  }


  .form-container{
      display: flex;
      justify-content: center;
      align-items: center;
      backdrop-filter: blur(20px);
      border-radius: 10px;
      padding-top: 20px; 
      margin-top: 1px;
      max-width: 400px;
      margin-left: auto;
      margin-right: auto;
      padding-bottom: 40px; 
}

  @media only screen and (min-width: 768px) {
    .container {
      flex-direction: row;
    }

    .container .content {
      width: 50%;
    }

    .loginn {
      width: 50%;
    }
  }
</style>
