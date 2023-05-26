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
    <div class="cars"> 
      <table>
        <thead>
          <tr style="color: antiquewhite;">
            <th>Car Number</th>
            <th>Date</th>
            <th>Entry Time</th>
            <!-- <th>Actions</th> -->
          </tr>
        </thead>    
        <tbody >
          <tr style="color: antiquewhite;" v-for="(car,index) in cars" :key="index">
             <td>
                <input v-model="car.Car_Number" @keyup.enter="saveCar(index)" />
              </td>
              <td>
                <input v-model="car.Date" @keyup.enter="saveCar(index)" />
              </td>
              <td>
                <input v-model="car.Time" @keyup.enter="saveCar(index)" />
              </td>
            <!-- <td>
              <button @click="editCar(car.id)">Edit</button>
              <button @click="deleteCar(car.id)">Delete</button>
            </td> -->
          </tr>
        </tbody>
       </table>
    </div>
 </body>   
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        cars: [],
        tempcars: [],
        isMobileMenuOpen: false
      };
    },
    mounted() {
      this.fetchCars();
    },
    methods: {
      fetchCars() {
        axios.get(`http://127.0.0.1:8000/carinfo/`)
          .then(response => {
            this.cars = response.data;
            this.tempcars =response.data.map(car => ({ ...car }));
          })
          .catch(error => {
            console.error(error);
          });
      },
      saveCar(index) {
      const car = this.cars[index];
      const previousCarNumber = this.tempcars[index].Car_Number; 

        axios.delete(`http://127.0.0.1:8000/car/${previousCarNumber}`)
          .then((response) => {
            console.log("deleted");
          })
        axios.post(`http://127.0.0.1:8000/car/${car.Car_Number}`,car)
        .then((response) => {
          console.log('Car saved successfully:', response.data);
          window.location.reload();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    toggleMobileMenu() {
    this.isMobileMenuOpen = !this.isMobileMenuOpen;
      }
    }
  };
  </script>
  
  <style>
  /* Add your CSS styles here */
  .body{
    background: url('/Users/gauravrastogi/Desktop/valet_parking_vue/valet/cosmic-2.jpg') no-repeat;
    /* padding-top: 90px; */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .cars{
    padding-top: 390px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10vh;
    backdrop-filter: blur(20px);
    max-width: 600px;
    /* padding-bottom: 40px; */
    margin-left: auto;
    margin-right: auto;
    max-height: 70vh;
     /* Adjust the height as per your preference */
    overflow-y: auto;
    overflow-x: scroll;
    scroll-snap-type: x mandatory;
    white-space: nowrap;
  }
  

  th {
    padding: 20px; /* Adjust the value as per your preference */
  }

  td {
    /* padding-bottom: 30px; Adjust the value as per your preference */
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
  
  .cars {
    padding-top: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1vh;
    backdrop-filter: blur(20px);
    max-width: 500px;
    max-height: 65vh;
     /* Adjust the height as per your preference */
    overflow-y: scroll;
    overflow-x: scroll;
  }
  th {
    padding: 30px; /* Adjust the value as per your preference */
    padding-left: 15%;
  }

  td {
    padding-left: 15%;
    /* padding-bottom: 30px; Adjust the value as per your preference */
  }

.cars > div:first-child {
    padding-left: calc((100vw - 100%) / 2);
    scroll-snap-align: start;  
  /* Adjust padding based on container width */
  } }
  </style>
  