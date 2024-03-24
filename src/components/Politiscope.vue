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

<div class="heading">
  <h3>{{ message }}</h3>
</div>

<div v-if="!dobPresent">
    <div class="input-container">
      <input class="day" type="text" v-model="day" placeholder="Day" maxlength="2">
      <input class="month" type="text" v-model="month" placeholder="Month" maxlength="2">
      <input class="year" type="text" v-model="year" placeholder="Year" maxlength="4">
    </div>
    <button class="save" @click="saveDateOfBirth">Save</button>
  </div>
  <div v-else> <!-- Second View -->
    
  </div>

</template>

<script>
import axios from 'axios';
export default {
data() {
  return {
    day: '',
    month: '',
    year: '',
    dateOfBirth: '',
    dobPresent : false,
    username : '',
    email : ''
  };
},
mounted(){
  this.username = sessionStorage.getItem('username');
  this.email = sessionStorage.getItem('email');
  this.checkDOB();
},
async created() {
  this.message = `Hello ${this.username}, enter your Date Of Birth.`;
},
methods: {
  async checkDOB() {
    // Make an Axios call to check if date of birth is present
    await axios.post('http://127.0.0.1:8003/checkdob', {  
      email: this.email},{
      headers: {
         'Content-Type': 'application/json', // Set Content-Type header to application/json
    }
  })
    .then(response => {
      if (response.status === 200) {
        // Assuming your backend responds with a boolean indicating whether DOB is present or not
        this.dobPresent = response.data;
        this.message = `Hello ${this.username}, this is your Politiscope`;
      }
      })
      .catch(error => {
        console.error('Error checking date of birth:', error);
        // Handle error accordingly
      });
  },
  async saveDateOfBirth() {
    const dateOfBirth = `${this.year}-${this.month.padStart(2, '0')}-${this.day.padStart(2, '0')}`;
    await axios.post('http://127.0.0.1:8003/storedob', {  
      email: this.email,
      dateOfBirth : dateOfBirth},{
      headers: {
         'Content-Type': 'application/json', // Set Content-Type header to application/json
    }
})
.then(response => {
    if (response.status === 200) {
      this.day = '';
      this.month = '';
      this.year = '';
      alert("Processing results . . .")
    } 
  })
  .catch(error => {
     if (error.response.status === 404) {
        // Handle HTTP 400 error (Bad Request) 
        alert("Something went wrong");
    } 
  });
}
}
};

</script>


<style>
.my-account {
margin-left: 20px; /* Adjust as needed */
}

.update-buttons {
margin-bottom: 20px; /* Add spacing between buttons and forms */
}

.update-buttons button {
margin-right: 10px; /* Add spacing between buttons */
}

.update-form {
margin-top: 20px; /* Add spacing between forms */
margin-left: 20px;
}

.email{
margin-right: 20px;
width: 340px;
height: 40px;
}

.old-password{
width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
}

.new-password{
width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;

}

.confirm-password{
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
}

.update-message {
color: green; /* Set color for success message */
margin-top: 10px; /* Add spacing below message */
}
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