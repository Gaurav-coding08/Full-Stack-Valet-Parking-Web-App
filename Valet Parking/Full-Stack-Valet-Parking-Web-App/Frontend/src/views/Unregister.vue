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
 <div v-if="showregist">
  <div class="containerr my-5">
    <!-- <div class="row justify-content-center"> -->
      <!-- <div class="col-md-6"> -->
        <!-- <div class="card"> -->
          <!-- <div class="card-header text-black"> -->
            <h3 class="card-title mb-0" style="color:white;">Car Unregistration</h3>
          <!-- </div> -->
          <!-- <div class="card-body"> -->
            <div v-if="showerrorMessage" class="alert alert-danger mt-3" role="alert">
               Car Not Registered So Could not be Deleted  From The Database!
            </div>
            <br>
            <form  >
              <div class="mb-3">
                <label for="car-number" class="form-label" style="color: white;">Car Number</label>
                <input type="text" class="form-control" id="car-number" name="car-number" placeholder="Enter Car Number" required pattern="[A-Za-z].*" title="Car Number Should Start With an Alphabet"  v-model="car_number">
              </div>
              <br>
              <div class="d-grid gap-2">
                <button type="button" class="btn btn-primary" @click="handleSubmit">Submit</button>
                <button type="button" class="btn btn-secondary" @click="reload">Cancel</button>
              </div>
            </form>
          <!-- </div> -->
        <!-- </div> -->
      <!-- </div> -->
    <!-- </div> -->
  </div>
 </div> 
 <div v-if="showeticket">
  <div class="containerr my-5">
   <!-- <div class="card text-center"> -->
    <!-- <div class="card-header">
      E-Ticket
    </div> -->
    <h3 class="card-title mb-0" style="color:white;">E-Ticket</h3>
    <!-- <div class="card-body"> -->
      <br>
      <p class="card-text" style="color:white;" >Car Number: {{ car_number }}</p>
      <p class="card-text" style="color:white;">Entry Time: {{ entryreptime }}</p>
      <p class="card-text" style="color:white;">Exit Time: {{ currentreptime }} </p>
      <p class="card-text" style="color:white;">Total Hours: {{ temphours }}</p>
      <p class="card-text" style="color:white;">Amount Calculated: {{ this.amount }}</p>
      <div class="d-grid gap-2 d-md-flex justify-content-md-center">
        <button class="btn btn-primary me-md-2 mb-2" type="button" @click="handlePayementReceived">Payment Received</button>
        <button class="btn btn-danger mb-2" type="button" @click="handlePayementNotReceived">Cancel</button>
      </div>
    <!-- </div> -->
      <br>
   </div>
  <!-- </div> -->
 </div>
 <div v-if="showSuccessMessage" class="alert alert-success mt-3" role="alert">
              Car Deleted Successfully From The Database!
 </div>
</body>
</template>


<script>
import { getAPI } from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/axios-api.js'
import axios from 'axios';
import router from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/src/router'

export default {
 name:'Unregister',
 components:{},
 data (){
  return {
    APIData:[],
    car_number:'',
    showSuccessMessage:false,
    showerrorMessage:false,
    costperhour:50,
    entrytime:'',
    entryreptime:'',
    currenttime:'',
    currentreptime:'',
    temphours:'',
    temp:'',
    amount:'',
    showregist:true,
    showeticket:false
  }
 },
  methods: {
    handleSubmit(event) {
      event.preventDefault();
      const confirmed = window.confirm("Are You Sure You want to Submit The Car Information")
      if (confirmed){
      const carNumber = this.car_number;

      // Make an API call to receive the data
      axios.get(`http://127.0.0.1:8000/car/${carNumber}`,)
        .then(response => {
          console.log('Data sent successfully');
          // Handle the response
          this.APIData = response.data;
          console.log(this.APIData);
          this.car_number=this.APIData.Car_Number;

          this.entrytime=this.APIData.Time;
          //entry time 
          const parts = this.entrytime.split(":");
          const hour = parseInt(parts[0], 10);
          const minutes = parseInt(parts[1], 10);
          this.entryreptime = `${hour}:${minutes}`;
          console.log("entry time rep",this.entrytimerep)
          this.entrytime = parseFloat(hour.toString() + '.' + minutes.toString());
          // const entryTimeFloat = (hour + minutes) / 60;
          console.log("entry time",this.entrytime)
          

          // Calculate the hour difference & current time
          const currentTime = new Date();
          const hourcurrent = parseInt(currentTime.getHours());
          const minutescurrent = parseInt(currentTime.getMinutes());
          this.currentreptime = `${hourcurrent}:${minutescurrent}`;
          const convertedTime = parseFloat(hourcurrent.toString() + '.' + minutescurrent.toString());
          this.currenttime=convertedTime
          
          this.temphours = hourcurrent-hour;
          const totaltimediff = convertedTime-this.entrytime;

          
          if (totaltimediff % 1 === 0) {
              this.amount=temphours * this.costperhour;
              console.log("first case")
          }
          else{
            if (totaltimediff < this.temphours){
                
                this.temphours=this.temphours-1.0;
                this.amount= this.temphours * this.costperhour;
                console.log("sec case")
            }
            else{
             
              this.temphours=this.temphours+1.0;
              this.amount= this.temphours * this.costperhour;
              console.log("third case")
            }
          }

          setTimeout(() => {
          this.showregist=false;
          this.showeticket=true;},2000
          //here
          )
        }) 
        .catch(error => {
          this.showregist=true;
          this.showerrorMessage=true;

          setTimeout(() => {
            this.$router.push('/Unregister');
            this.resetData();
              }, 1000);
        });
    }
      else{
        this.$router.push('/Unregister');
        this.resetData();
      }
  },
  handlePayementReceived(event){
    // this.showeticket=false;
    // this.showSuccessMessage=true;
    axios.delete(`http://127.0.0.1:8000/car/${this.car_number}`,)
    .then(response => {
      this.showeticket=false;
      this.showSuccessMessage=true;
      setTimeout(() => {
      this.$router.push('/Services');
      this.resetData();
      }, 2000);
    })
    .catch(error => {
          // console.error('Car could not be deleted');
          // Handle the error
          this.showerrorMessage=true;

          this.showeticket=false;
          setTimeout(() => {
            this.$router.push('/Unregister');
            this.resetData();
              }, 2000);

        });
  },
  handlePayementNotReceived(event){
    this.$router.push('/Unregister');
    this.resetData();
  },
  resetData(){
    this.APIData=[],
    this.car_number='',
    this.showSuccessMessage=false,
    this.showerrorMessage=false,
    this.costperhour=50,
    this.entrytime='',
    this.entryreptime='',
    this.currenttime='',
    this.currentreptime='',
    this.temphours='',
    this.temp='',
    this.amount='',
    this.showregist=true,
    this.showeticket=false
  },
  reload(){
    this.$router.push('/Unregister');
    this.resetData();
  }
  }
}
</script>

<style>
.containerr{
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