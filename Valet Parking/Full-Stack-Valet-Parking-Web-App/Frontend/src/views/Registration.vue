<template>
<body>
  <nav >
    <router-link to="/" :class="{ 'custom-link-active': $route.path === '/' }">Login</router-link> |
    <router-link to="/Services" :class="{ 'custom-link-active': $route.path === '/Services' }">Services</router-link> |
    <router-link to="/Registration" :class="{ 'custom-link-active': $route.path === '/Registration' }">Registration</router-link> |
    <router-link to="/Unregister" :class="{ 'custom-link-active': $route.path === '/Unregister' }">Unregistration</router-link> |
    <router-link to="/Employeeregis" :class="{ 'custom-link-active': $route.path === '/Employeeregis' }">New Employee Registration</router-link> |
    <router-link to="/edit_seecars" :class="{ 'custom-link-active': $route.path === '/edit_seecars' }">Edit & View Cars</router-link>
  </nav>
  <div v-if="showregistr">
   <div class="containerrr my-5">
    <!-- <div class="row justify-content-center"> -->
      <!-- <div class="col-md-6"> -->
        <!-- <div class="card"> -->
          <!-- <div class="card-header text-black"> -->
            <h3 class="card-title mb-0" style="color:white;"> Car Registration</h3>
          <!-- </div> -->
          <!-- <div class="card-body"> -->
            <br>
            <div v-if="showSuccessMessage" class="alert alert-success mt-3" role="alert">
              Data sent successfully!
            </div>
            <form>
              <!-- <div class="mb-3"> -->
                <label for="car-number" class="form-label" style="color: white;">Car Number</label>
                <input type="text" class="form-control"  placeholder="Enter car number" required pattern="[A-Za-z].*" title="Car Number Should Start With an Alphabet" v-model="car_number">
              <!-- </div> -->
              <!-- <div class="mb-3"> -->
                <br>
                <label for="date" class="form-label" style="color: white;">Date</label>
                <input type="date" class="form-control" required v-model="date">
              <!-- </div> -->
              <!-- <div class="mb-3"> -->
                <br>
                <label for="time" class="form-label" style="color: white;">Time</label>
                <input type="time" class="form-control"  required v-model="time">
              <!-- </div> -->
                <br>
              <div class="mb-3 d-grid gap-2">
                <button type="button" class="btn btn-primary" @click="handleSubmit">Submit</button>
                <button type="reset" class="btn btn-secondary">Reset</button>
              </div>
            </form>
          <!-- </div> -->
        <!-- </div> -->
      <!-- </div> -->
    <!-- </div> -->
   </div>
  </div>
  <div v-if="showerrorMessage" class="alert alert-danger mt-3" role="alert">
    Invalid Car Number! Please Try Again
  </div>
</body>
</template>

<script>
import { getAPI } from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/axios-api.js'
import axios from 'axios';

export default {
 name:'Registration',
 data (){
  return {
    APIData:[],
    car_number:'',
    time: '',
    date:'',
    showSuccessMessage:false,
    showerrorMessage:false,
    // isLoggedIn:false,
    showregistr:true
  }
 },
 
  // mounted(){
  //   // const tempLoggedIn=false
  //   localStorage.setItem('isLoggedIn', false)
  //   // if (this.tempLoggedIn=="false"){
  //   //   localStorage.setItem('isLoggedIn', false);
  //   // }
  // },
  methods: {
    handleSubmit(event) {
      event.preventDefault();
      const confirmed = window.confirm("Are You Sure You want to Submit The Car Information")
      if (confirmed){
      const carNumber = this.car_number;
      const time = this.time;
      const date = this.date;

      // Make an API call to send the data
      axios.post(`http://127.0.0.1:8000/car/${carNumber}`, {
        Car_Number: carNumber,
        Time: time,
        Date: date
      })
        .then(response => {
          console.log('Data sent successfully');
          // Handle the response
          // this.APIData = response.data;
          // console.log(this.APIData.Car_Number);
          this.showSuccessMessage=true;
          setTimeout(() => {
        this.resetData();
      }, 1000);
        })
        .catch(error => {
          console.error('Error sending data:', error);
          // Handle the error
          this.showregistr=false;
          this.showerrorMessage=true
          setTimeout(() => {
            this.resetData();
            this.$router.push('/Registration');
      },2000);
        })
        }
      else{
        this.$router.push('/Registration');
        this.resetData();
      }
  },
  resetData(){
    this.APIData=[],
    this.car_number='',
    this.time= '',
    this.date='',
    this.showSuccessMessage=false,
    this.showerrorMessage=false,
    this.showregistr=true
  }
  }
}

</script>
<style>
.containerrr{
      backdrop-filter: blur(20px);
      /* background-color: white; */
      border-radius: 10px;
      padding: 30px;
      margin-top: 100px;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
}

</style>