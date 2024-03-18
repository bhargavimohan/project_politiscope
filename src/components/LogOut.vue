<template>
    <!-- <h1>Hello User! This is your home page</h1> -->
  <!-- Background overlay -->

  
  <!-- Navbar -->
  <nav class="navbar">
    <router-link to="/politiscope">PolitiScope</router-link>
    <router-link to="/myaccount">My account</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/infocenter">Info</router-link>
    <router-link to="/logout"><b><u>Log out</u></b></router-link>
  </nav>
</template>

<script>

export default {
    name: 'InfoCenter'
}
</script>

<style>
    
   
    
    /* Navbar styling */
    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      width: 200px;
      height: 100%;
      background-color: #0b0b0b; /* Adjust navbar background color */

    }
    
    /* Navbar links styling */
    .navbar a {
      display: block;
      padding: 10px;
      text-decoration: none;
      color: #f0ecec; /* Adjust link color */
    }
    
    /* Navbar link hover effect */
    .navbar a:hover {
      background-color: #0b0b0b; /* Adjust hover background color */
      font-weight: bold;
    }
  </style>