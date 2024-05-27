<template>
  <div class="main-container">
    <h1>Добро пожаловать в сервис подбора факультета</h1>
    <p class="info-text">Наш ВУЗ — один из ведущих технических вузов России. Подготовка студентов ведётся по самым
      актуальным направлениям в области радиотехники, электронной и вычислительной техники, программирования, автоматики
      и систем управления, информационных технологий, информационной безопасности, инноватики, экономики и социальной
      работы. Выбирая одно из них, вы выбираете своё будущее.</p>

    <div class="form-container">
      <h2>Заполните форму для подбора факультета</h2>
      <form @submit.prevent="getFaculties">
        <div class="form-group">
          <label>Любимые предметы в школе:</label>
          <input type="text" v-model="favorite_subjects" placeholder="Введите предметы через запятую" />
        </div>
        <div class="form-group">
          <label>Нелюбимые предметы в школе:</label>
          <input type="text" v-model="leastFavoriteSubjects" placeholder="Введите предметы через запятую" />
        </div>
        <div class="form-group">
          <label>Экзамены:</label>
          <input type="text" v-model="exams" placeholder="Введите экзамены через запятую" />
        </div>
        <div class="form-group">
          <label>Мне интересно:</label>
          <textarea v-model="interests" placeholder="Расскажите, что вам интересно"></textarea>
        </div>
        <div class="form-group">
          <label>Мне неинтересно:</label>
          <textarea v-model="disinterests" placeholder="Расскажите, что вам неинтересно"></textarea>
        </div>
        <div class="form-group">
          <label>Результат:</label>
          <textarea v-model="result"></textarea>
        </div>
        <button type="submit">Подобрать факультет</button>
      </form>
    </div>
  </div>
</template>
<style scoped></style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      favorite_subjects: '',
      leastFavoriteSubjects: '',
      exams: '',
      interests: '',
      disinterests: '',
      result: '',
      error: ''
    }
  },
    methods: {
      async getFaculties() {

        try {
        const response = await axios.post('/facultyselection', {
          favorite_subjects : this.favorite_subjects,
        })
        console.log(response.data)
        if (response.data.error) {
          this.error = response.data.error;
        } 
        else if (response.data.result) {
          this.result = response.data.result
        }
      } 
      
      catch (error) {
        this.error = error.response && error.response.data.error ? error.response.data.error : '';
      }
    }
  }
};
</script>

<style scoped>
.main-container {
  margin: auto;
  max-width: 1170px;
  background-color: white;
  color: #3C388D;
  padding: 20px;
  font-family: Arial, sans-serif;
  position: relative;
}

h1 {
  font-size: 2em;
  text-align: center;
  margin-bottom: 0.5em;
}

.info-text {
  color: #5F5F5F;
  margin-bottom: 2em;
  text-align: center;
}

.form-container {
  width: 75%;
  margin: auto;
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
  width: 98%;
  padding: 0.5em;
  border: 1px solid #CCC;
  border-radius: 4px;
  margin-bottom: 0.5em;
  height: 2em;
  resize: none;
}

textarea {
  height: 8em;
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