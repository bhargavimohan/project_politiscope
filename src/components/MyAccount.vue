<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar">
      <router-link to="/politiscope">PolitiScope</router-link>
      <router-link to="/myaccount"><b><u>My account</u></b></router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/infocenter">Info</router-link>
      <router-link to="/logout">Log out</router-link>
    </nav>

    <div class="my-account">
      <h1>Welcome, {{ username }}!</h1>
      
      <div class="update-buttons">
        <button @click="showEmailForm">Update Email</button>
        <button @click="showPasswordForm">Update Password</button>
      </div>
      
      <!-- Update Email Form -->
      <div v-if="showEmail">
        <h2>Update Email</h2>
        <form @submit.prevent="updateEmail">
          <input class="email" type="email" v-model="newEmail" placeholder="New Email">
          <button type="submit">Update</button>
          <p v-if="!newEmail" class="error-message">{{ emailErrMessage }}</p>
        </form>
        <p v-if="emailUpdateMessage" class="update-message">{{ emailUpdateMessage }}</p>
      </div>
      
      <!-- Update Password Form -->
      <div v-if="showPassword">
        <h2>Update Password</h2>
        <form @submit.prevent="updatePassword">
          <input class="new-password" type="password" v-model="newPassword" placeholder="New Password">
          <input class="confirm-password" type="password" v-model="confirmPassword" placeholder="Confirm Password">
          <button type="submit">Update</button>
          <p v-if="!newPassword" class="error-message">{{ pwdErrMsg }}</p>
        </form>
        <p v-if="passwordUpdateMessage" class="update-message">{{ passwordUpdateMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      current_email: '',
      username: '',
      newEmail: '',
      newPassword: '',
      confirmPassword: '',
      showEmail: false,
      showPassword: false,
      emailUpdateMessage: '',
      emailErrMessage : '',
      pwdErrMsg : '',
      passwordUpdateMessage: ''
    };
  },
  mounted() {
    this.username = sessionStorage.getItem('username');
    this.current_email = sessionStorage.getItem('email');
  },
  methods: {
    showEmailForm() {
      this.showEmail = true;
      this.showPassword = false; // Hide password form
    },
    showPasswordForm() {
      this.showPassword = true;
      this.showEmail = false; // Hide email form
    },
    async updateEmail() {
      if (!this.newEmail) {
        this.emailErrMessage = 'Email is required';
        return; // Don't proceed if email is empty
      }
      // Make an Axios call to update email
      try {
        const response = await axios.put('http://127.0.0.1:8003/update-email', {
          oldEmail: this.current_email,
          newEmail: this.newEmail
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (response.status === 200) {
          this.emailUpdateMessage = 'Email updated successfully, you will be redirected to Login page, please login again';
          this.emailErrMessage = ''
          this.newEmail = '';
          // Hide message after some time (e.g., 3 seconds)
          setTimeout(() => {
        this.emailUpdateMessage = '';
        // Redirect to login page after 10 seconds
        setTimeout(() => {
          // Assuming router is imported and initialized properly
          this.$router.push('/login'); // Change '/login' to your actual login route
        }, 2000); // 5 seconds
      }, 3000); // 3 seconds
    }
      } catch (error) {
        console.error('Error updating email:', error);
        // Handle error accordingly
      }
    },
    async updatePassword() {
      if (!this.newPassword) {
        this.pwdErrMsg = 'All the fields are required';
        return; // Don't proceed if new password is empty
      }
      if (this.newPassword !== this.confirmPassword) {
        this.pwdErrMsg = 'New Passwords do not match';
        this.newPassword = ''
        this.confirmPassword = ''
        return; // Don't proceed if passwords don't match
      }
      // Make an Axios call to update password
      try {
        const response = await axios.put('http://127.0.0.1:8003/update-password', {
          currentEmail: this.current_email,
          newPassword: this.newPassword,
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (response.status === 200) {
          this.passwordUpdateMessage = 'Password updated successfully';
          this.pwdErrMsg = ''
          // Clear input fields after update
          this.newPassword = '';
          this.confirmPassword = '';
          // Hide message after some time (e.g., 3 seconds)
          setTimeout(() => {
            this.passwordUpdateMessage = '';
          }, 3000);
        }
      } catch (error) {
        console.error('Error updating password:', error);
        // Handle error accordingly
      }
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
    margin-right: auto
}

.update-message{
  color: green;
  font-weight: bold;
}

.error-message{
  color: red;
  font-weight: bold;
}

</style>