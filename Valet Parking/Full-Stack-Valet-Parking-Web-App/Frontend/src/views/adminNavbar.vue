<template>
  <nav>
    <router-link to="/">Login</router-link> |
    <router-link to="/Services">Services</router-link> |
    <router-link to="/Registration">Registration</router-link> |
    <router-link to="/Unregister">Unregister</router-link>
  </nav>
  <router-view/>
</template>

<script>
export default {
    name: 'adminNav'
}
</script>

<style>

</style>