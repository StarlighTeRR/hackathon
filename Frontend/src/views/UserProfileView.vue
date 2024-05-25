<template>
  <div class="main-container">
    <h1>Профиль пользователя</h1>
    <form @submit.prevent="submitForm" class="form-container">
      <div class="form-group">
        <label for="lastName">Фото</label>
        <div class="file-upload">
          <input type="file" id="photo" @change="handleFileUpload" />
          <label for="photo" class="button-photo">Выбрать файл</label>
          <span class="file-name" id="file-name">Файл не выбран</span>
        </div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input type="text" id="id" v-model="user.id" disabled style="background-color: #e0e0e0; color: #6d6d6d;" />
      </div>
      <div class="form-group">
        <label for="lastName">Фамилия</label>
        <input type="text" id="lastName" v-model="user.lastName" required />
      </div>
      <div class="form-group">
        <label for="firstName">Имя</label>
        <input type="text" id="firstName" v-model="user.firstName" required />
      </div>
      <div class="form-group">
        <label for="middleName">Отчество</label>
        <input type="text" id="middleName" v-model="user.middleName" required />
      </div>
      <div class="form-group">
        <label for="birthDate">Дата рождения</label>
        <input type="date" id="birthDate" v-model="user.birthDate" required />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="user.email" required />
      </div>
      <div class="form-group">
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <div>
        <label for="confirmPassword">Подтверждение пароля</label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" />
      </div>
      <div v-if="passwordMismatch" class="error">Пароли не совпадают</div>
      <button type="submit">Сохранить</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        id: '12345',
        lastName: '',
        firstName: '',
        middleName: '',
        birthDate: '',
        email: '',
      },
      password: '',
      confirmPassword: '',
      photo: null,
      passwordMismatch: false,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.photo = event.target.files[0];
    },
    submitForm() {
      if (this.password !== this.confirmPassword) {
        this.passwordMismatch = true;
        return;
      }
      this.passwordMismatch = false;
      // Сохранение данных пользователя
    },
  },
};
</script>

<style scoped>
.error {
  color: red;
}

.main-container {
  margin: 0 auto;
  max-width: 1170px;
  background-color: white;
  color: #3C388D;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  font-size: 2em;
  text-align: center;
  margin-bottom: 0.5em;
  font-family: "NekstRegular", "Verdana", sans-serif;
}

.info-text {
  color: #5F5F5F;
  margin-bottom: 2em;
  font-family: "NekstRegular", "Verdana", sans-serif;
}

.form-container {
  width: 75%;
  margin: 0 auto;
}

h2 {
  font-size: 1.5em;
  margin-bottom: 1em;
  text-align: center;
}

.form-group {
  margin-bottom: 1em;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5em;
}

input,
textarea {
  width: 100%;
  padding: 0.3em;
  border: 1px solid #CCC;
  border-radius: 4px;
  margin-bottom: 0.5em;
  height: 2em;
  font-size: 16px;
  padding-left: 7px;
}

textarea {
  height: 8em;
}

.file-upload {
  position: relative;
  display: inline-block;
}

.file-upload input[type="file"] {
  display: none;
}

.file-upload label {
  display: inline-block;
  background-color: #9fc53a;
  color: white;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.file-upload label:hover {
  background-color: #3c388d;
  color: white;
}

.file-name {
  margin-left: 10px;
  font-style: italic;
}

button {
  padding: 0.5em 1em;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: block;
  width: 100%;
  font-size: 1em;
}

button:hover {
  background-color: #0056b3;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 1em;
}

li button {
  margin-left: 1em;
  background-color: #28a745;
}

li button:hover {
  background-color: #218838;
}
</style>