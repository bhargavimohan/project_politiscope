<!-- Signup.vue -->
<template>
  <div>
    <img class="image" src="../assets/politiscopev1nobg.png"/>
  </div>
<!-- 
  <div class="heading">
    <h5>Create a new Politiscope account</h5>
  </div> -->
  <div class="sign-up">
    <h5>Create a new Politiscope account or <router-link to="/login" class="roter-login">Login </router-link></h5> 
    <input class="orange" v-model="name" type="text" placeholder="Enter Name">
    <input class="white" v-model="email" type="text" placeholder="Enter Email">
    <input class="green" v-model="password" type="password" placeholder="Enter Password">
    <button v-on:click="signupForm">Sign Up</button>
</div>

</template>

<script>
export default {
data() {
  return {
    name: '',
    email: '',
    password: ''
  };
},
methods: {
  signupForm() {
    fetch('http://127.0.0.1:8003/sign-up', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: this.name,
        email: this.email,
        password: this.password,
      }),
      
    })
    .then(response => {
    if (response && response.status === 200) {
      // Sign up was successful, display an alert
      alert('Sign up successful!');
      
      // Redirect users to another page (e.g., using Vue Router)
      this.$router.push('/another-page');
    } else {
      // Handle other response statuses or undefined response
      // For example, if you receive a non-200 status or the response is undefined,
      // you might want to display an error message or take appropriate action.
      alert('Sign up failed!');
    }
  })
    .catch(error => {
      console.error('Error:', error);
    });
  }
}
};
</script>

<style> 

.image{
width: 400px;
margin-left: 300px;
margin-top: -60px;
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
margin-left: 450px;
margin-top: 200px;

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

.white{
width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid blue;
  color: blue;
 
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