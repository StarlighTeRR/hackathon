<template>
    <section class="sign">
      <div class="container">
        <div class="sign-content">
          <div class="sign-form">
            <h2 class="form-title">Вход</h2>
            <form class="register-form" @submit.prevent="Authentificate">
              <div class="form-group">
                <input type="email" v-model="email" placeholder="Логин (email)" required>
              </div>
              <div class="form-group">
                <input type="password" v-model="password" placeholder="Пароль" required>
              </div>
              <div v-if="error" class="error-message">{{ error }}</div>
              <div class="form-container">
                <div class="form-group form-button">
                  <input type="submit" class="form-submit" value="Войти">
                </div>
                <div class="form-button">
                  <button type="button" class="form-submit" @click="$router.push({ name: 'register' })">Регистрация</button>
                </div>
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
        password: '',
        error: ''
      };
    },
    methods: {
      ...mapActions(['saveAuthToken']),
      async Authentificate() {
        if (this.isPasswordValid(this.password)) {
            this.error = ''

            try {
        const response = await axios.post('/login', {
          email: this.email,
          password: this.password,
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
        } 
        else {
          this.error = 'Пароль латинские буквы и цифры, длина не менее 8 символов';
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
    min-width: max-content;
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
    /* Цвет фона для секции, вы можете изменить его при необходимости */
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
  
  .form-group,
  .form-button {
    flex: 1;
    margin-right: 10px;
    margin-bottom: 15px;
  }
  
  .form-group:last-child,
  .form-button:last-child {
    margin-right: 0;
  }
  
  .form-submit {
    width: 100%;
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
    /* Убираем стрелки для выбора даты */
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
  }
  
  .form-group input[type="checkbox"] {
    margin-right: 10px;
  }
  
  .form-container {
    display: flex;
    justify-content: space-between;
    width: 100%;
  }
  
  .label-agree-term {
    font-size: 14px;
    color: #333;
  }
  
  .label-agree-term a {
    color: #3C388D;
    text-decoration: none;
  }
  
  .label-agree-term a:hover {
    text-decoration: underline;
  }
  
  .form-button {
    display: flex;
    justify-content: center;
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
    color: rgb(185, 22, 22);
    margin-bottom: 15px;
    text-align: center;
    font-family: Poppins;
  }
  </style>
  