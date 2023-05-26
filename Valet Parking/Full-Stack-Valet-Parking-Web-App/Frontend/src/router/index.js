import { createRouter, createWebHistory } from 'vue-router'
import Services from '../views/Services.vue'
import Home from '../views/Home.vue'
import Registration from '../views/Registration.vue'
import Unregister from '../views/Unregister.vue'
// import Generate_E_Ticket from '../views/Generate_E_Ticket.vue'
import Employeeregis from '../views/Employeeregis.vue'
import edit_seecars from '../views/edit_seecars.vue'
import Dataanal from '../views/Dataanal.vue'
// Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/Services',
    name: 'Services',
    component:Services,
    meta: { requiresAuth: true }
  },
  {
    path: '/Registration',
    name: 'Registration',
    component:Registration,
    meta: { requiresAuth: true }
  },
  {
    path: '/Unregister',
    name: 'Unregister',
    component:Unregister,
    meta: { requiresAuth: true }
  },
  // {
  //   path: '/Generate_E_Ticket',
  //   name: 'Generate_E_Ticket',
  //   component:Generate_E_Ticket,
  //   meta: { requiresAuth: true }
  // },
  {
    path: '/Employeeregis',
    name: 'Employeeregis',
    component:Employeeregis,
    meta: { requiresAuth: true }
  },
  {
    path: '/edit_seecars',
    name: 'edit_seecars',
    component:edit_seecars,
    meta: { requiresAuth: true }
  },
  {
    path: '/Dataanal',
    name: 'Dataanal',
    component:Dataanal,
    meta: { requiresAuth: true }
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  // mode: 'history',
  routes,
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && isLoggedIn === 'true') {
    // If the route requires authentication and the user is logged in,
    // allow access to the route
    next();
  } else if (requiresAuth && isLoggedIn !== 'true'){
    // If the user is accessing the login page, set isLoggedIn to false
    // to ensure they are not considered logged in
    // localStorage.setItem('isLoggedIn', 'false');
    next('/');
  } else {
    // If the route requires authentication and the user is not logged in,
    // or if it's any other route, redirect to the home page or another appropriate route
    next();
  }
});


export default router
