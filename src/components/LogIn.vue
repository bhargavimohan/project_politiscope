<!-- Signup.vue -->
<template>
  <div>
    <img class="image" src="../assets/POLITISCOPE-removebg.png"/>
  </div>
<!-- 
  <div class="heading">
    <h5>Create a new Politiscope account</h5>
  </div> -->
  <div class="sign-up">
    <h4>Log in</h4> 
    <input class="orange" v-model="email" type="text" placeholder="Enter Email">
    <input class="green" v-model="password" type="password" placeholder="Enter Password">
    <button v-on:click="loginForm()">Login</button>
    <h5>New to Politiscope? <router-link to="/signup" class="roter-login">Sign Up</router-link></h5>
</div>

</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async loginForm() {
      await axios.post('http://127.0.0.1:8003/login', {
        
          email: this.email,
          password: this.password},{
          headers: {
             'Content-Type': 'application/json', // Set Content-Type header to application/json
        }
    })
      .then(response => {
      if (response.status === 200) {
        // Sign up was successful, display an alert
        alert('Login successful!');
        // Redirect users to another page (e.g., using Vue Router)
        sessionStorage.setItem('username' , response.data['username']);
        sessionStorage.setItem('email' , response.data['email']);
        
        this.$router.push('/politiscope');
      } 
    })
    .catch(error => {
       if (error.response.status === 400) {
          // Handle HTTP 400 error (Bad Request) 
          alert(this.email + " is not registered");
          this.$router.push('/signup');
      } 
      else if (error.response.status === 401) {
          // Handle HTTP 400 error (Bad Request)
          alert("Invalid password. Please enter the right password.");
          this.password = ''
          this.$router.push('/login');
      } 
      else {
        // Handle other response statuses or undefined response
        // For example, if you receive a non-200 status or the response is undefined,
        // you might want to display an error message or take appropriate action.
        alert('Sign up failed!');
      }
      });
    }
  }
};
</script>

<style> 

.image{
  width: 800px;
  margin-left: 100px;
  margin-top: -300px;
  display: flex;
  justify-content: center; /* Horizontally center the content */
  align-items: center; /* Vertically center the content */
  position: absolute; /* Set container position to relative for absolute positioning */
}

.h5 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: black; /* Set the font color */
  /*text-align: center;  Align the text to the center */
  /* padding-left: 450px; */
}

.sign-up{
  position: relative;
  margin-left: 550px;
  margin-top: 250px;

}
.orange{
  width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 1px ;
    background-color: rgb(246, 165, 58);
    color: black;
    
}

.green{
  width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 1px ;
    background-color:  rgb(107, 209, 107);
    color: black;
  
}

.sign-up button{
  width: 200px;
  height: 20px;
  cursor: pointer;
  background-color: white;
  
}

.roter-login{
  color: black;
}
</style>