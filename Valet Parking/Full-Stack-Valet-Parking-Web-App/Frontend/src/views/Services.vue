<template>
 <body>
  <nav>
    <router-link to="/" :class="{ 'custom-link-active': $route.path === '/' }">Login</router-link> |
    <router-link to="/Services" :class="{ 'custom-link-active': $route.path === '/Services' }">Services</router-link> |
    <router-link to="/Registration" :class="{ 'custom-link-active': $route.path === '/Registration' }">Registration</router-link> |
    <router-link to="/Unregister" :class="{ 'custom-link-active': $route.path === '/Unregister' }">Unregistration</router-link> |
    <router-link to="/Employeeregis" :class="{ 'custom-link-active': $route.path === '/Employeeregis' }">New Employee Registration</router-link> |
    <router-link to="/edit_seecars" :class="{ 'custom-link-active': $route.path === '/edit_seecars' }">Edit & View Cars</router-link>
  </nav>
  <div class="containerrrr">
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <div class="options-container" :class="{ 'slide-in': showOptions }">
          <h2 class="text-center mb-4" style="color:white;">Features</h2>
          <ul class="list-group blurred-bg" style="color:rgb(244, 235, 235);">
            <li class="list-group-item" >
              <router-link to="/Registration" class="text-decoration-none" style="color:black;" >Register Car</router-link>
            </li>
            <li class="list-group-item">
              <router-link to="/Unregister" class="text-decoration-none" style="color:black;">Unregister Car</router-link>
            </li>     
            <li class="list-group-item">
              <router-link to="/edit_seecars" class="text-decoration-none" style="color:black;">Edit & View Car Info</router-link>
            </li>  
            <li class="list-group-item">
              <router-link to="/Employeeregis" class="text-decoration-none" style="color:black;">New Employee Registration</router-link>
            </li> 
            <li class="list-group-item">
              <router-link to="/Services" class="text-decoration-none" style="color:black;">Data Analytics</router-link>
            </li> 
          </ul>
        </div>
      </div>
    </div>
  </div>
 </body>
</template>

<script>
// import adminNav from '/Users/gauravrastogi/Desktop/valet_parking_vue/valet/src/views/adminNavbar.vue'
export default {
  name: 'Services',
  data() {
  return {
    showOptions: false
  }
},
mounted() {
  setTimeout(() => {
    this.showOptions = true;
  }, 100);
}
}

</script>
<style>
    .options-container {
      backdrop-filter: blur(20px);
      /* background-color: white; */
      border-radius: 10px;
      padding: 30px;
      margin-top: 100px;
      max-width: 400px;
      margin-left: auto;
      margin-right: auto;
    }
    .blurred-bg {
  background-color: transparent; /* Adjust the alpha value to control the level of blur */
  opacity: 0.8; /* Adjust the opacity value to control the level of blur */
  box-shadow: 0 0 10px rgba(194, 29, 67, 0.899); /* Adjust the shadow properties as desired */
}

.options-container {
  opacity: 0;
  transform: translateX(-100%);
  transition: opacity 0.5s ease-in, transform 0.5s ease-in;
}

.slide-in {
  opacity: 1;
  transform: translateX(0);
}
    .custom-link{
      color: #42b983;
    }
    nav a {
     color: white;
     text-decoration: none;
     padding: 8px 12px;
     margin-right: 10px;
   }
    @media (max-width: 576px) {
      .options-container {
        margin-top: 50px;
      }
    }
  </style>
