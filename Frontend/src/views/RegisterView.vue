<template>
    <section class="sign">
      <div class="container">
        <div class="sign-content">
          <div class="sign-form">
            <h2 class="form-title">Регистрация</h2>
            <form class="register-form" @submit.prevent="registrate">
              <div class="form-group">
                <input type="email" v-model="email" placeholder="Логин (e-mail)" required>
              </div>
              <div class="form-group">
                <input type="text" v-model="last_name" placeholder="Фамилия" required />
              </div>
              <div class="form-group">
                <input type="text" v-model="name" placeholder="Имя" required />
              </div>
              <div class="form-group">
                <input type="text" v-model="middle_name" placeholder="Отчество" required />
              </div>
              <div class="form-group">
                <input type="date" v-model="birth_date" placeholder="Дата рождения" required />
              </div>
              <div class="form-group">
                <input type="password" v-model="password" placeholder="Пароль" required />
              </div>
              <div class="form-group">
                <input type="password" v-model="confirm_password" placeholder="Подтверждение пароля" required />
              </div>
              <div v-if="error" class="error-message">{{ error }}</div>
              <div class="form-group form-button">
                <input type="submit" name="sign" id="sign" class="form-submit" value="Зарегистрироваться" />
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import axios from 'axios';
import { mapActions, mapGetters } from 'vuex';

  export default {
    computed: {
    ...mapGetters(['isAuthenticated'])
  },
    data() {
      return {
        email: '',
        name: '',
        last_name: '',
        middle_name: '',
        birth_date: '',
        password: '',
        error: ''
      };
    },
    methods: {
      ...mapActions(['saveAuthToken']),

      async registrate() {
        this.error = '';
  
        if (this.password !== this.confirm_password) {
          this.error = 'Пароли не совпадают';
          return;
        }
  
        if (!this.isPasswordValid(this.password)) {
          this.error = 'Пароль должен содержать хотя бы 8 латинских букв или цифр';
          return;
        }

      try {
        const response = await axios.post('/register', {
          email: this.email,
          name: this.name,
          last_name: this.last_name,
          middle_name: this.middle_name,
          birth_date: this.birth_date,
          password: this.password
        })
        if (response.data.error) {
          this.error = response.data.error;
        } 
        else if (response.data.token) {
          this.saveAuthToken(response.data.token)
          this.$router.push({name: 'home'})
        }
      } 
      catch (error) {
        this.error = error.response && error.response.data.error ? error.response.data.error : '';
      }
    },
      isPasswordValid(password) {
        const passwordRegex = /^[A-Za-z0-9]{8,}$/;
        return passwordRegex.test(password);
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    width: 20%;
    padding: 20px;
    background: #fff;
    border-radius: 10px;
    display: flex;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }
  
  /* Основные стили для секции регистрации */
  .sign {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
    background-color: #f2f2f2;
  }
  
  .sign-content {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  
  .sign-form {
    width: 100%;
  }
  
  .form-title {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .form-group {
    position: relative;
    margin-bottom: 15px;
  }
  
  .form-group input[type="text"],
  .form-group input[type="email"],
  .form-group input[type="password"] {
    border-radius: 5px;
    background: #f9f9f9;
    width: 100%;
    height: 40px;
    display: block;
    border: none;
    border-bottom: 1px solid #999;
    padding: 6px 10px;
    font-family: 20px Poppins;
    box-sizing: border-box;
  }
  
  .form-group input[type="date"] {
    border-radius: 5px;
    background: #f9f9f9;
    width: 100%;
    display: block;
    border: none;
    border-bottom: 1px solid #999;
    padding: 6px 10px;
    font-family: Poppins;
    box-sizing: border-box;
  }
  
input, textarea {
    width: 100%;
    padding: 0.5em;
    border: 1px solid #CCC;
    border-radius: 4px;
    margin-bottom: 0.5em;
    padding: 0.5em;
    height: 2em;
  }

  select {
    width: 100px;
    box-sizing: border-box;
    padding: 0.5em;
    border: 1px solid #CCC;
    border-radius: 4px;
    margin-bottom: 0.5em;
    height: auto;
  }

  .form-button {
    display: flex;
    justify-content: center;
    width: 100%;
    margin: 0;
  }
  
  .form-submit {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background: #3C388D;
    color: #fff;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s;
  }
  
  .form-submit:hover {
    background: #2e2a72;
  }
  
  .error-message {
    color: red;
    margin-bottom: 15px;
    text-align: center;
  }
  
  /* Иконки внутри формы */
  .form-group i {
    position: absolute;
    top: 50%;
    left: 10px;
    transform: translateY(-50%);
    color: #333;
  }
  </style>
  