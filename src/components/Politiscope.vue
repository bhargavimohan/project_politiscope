<template>
    <!-- <h1>Hello User! This is your home page</h1> -->
  <!-- Background overlay -->

  
  <!-- Navbar -->
  <nav class="navbar">
    <router-link to="/politiscope"><b><u>Politiscope</u></b></router-link>
    <router-link to="/myaccount">My account</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/infocenter">Info</router-link>
    <router-link to="/logout">Log out</router-link>
  </nav>

</template>

<script>

export default {
  mounted() {
const userName = localStorage.getItem('username');
if (userName) {
  console.log(userName); // Output: User Name
} else {
  console.log('User name not found in local storage');
}
  }

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
      color: #090909; /* Adjust link color */
    }
    
    /* Navbar link hover effect */
    .navbar a:hover {
      background-color: #ede5e5; /* Adjust hover background color */
      font-weight: bold;
    }
  </style>