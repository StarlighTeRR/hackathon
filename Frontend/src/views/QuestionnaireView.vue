<template>
    <div class="main-container">
        <div class="form-group form-container">
            <h1>Моя анкета</h1>
            <div>
                <p>Ваша заявка успешно отправлена. Мы свяжемся с вами в ближайшее время по указанным вами контактам.</p>
                <button type="button" @click="editApplication">Подать заявку заново</button>
            </div>
        </div>
        <form class="form-container" @submit.prevent="submitApplication">
            <div class="form-group">
                <label for="lastName">Фамилия</label>
                <input type="text" id="lastName" v-model="form.lastName" disabled />
            </div>
            <div class="form-group">
                <label for="firstName">Имя</label>
                <input type="text" id="firstName" v-model="form.firstName" disabled />
            </div>
            <div class="form-group">
                <label for="middleName">Отчество</label>
                <input type="text" id="middleName" v-model="form.middleName" disabled />
            </div>
            <div className="form-group">
                <label for="birthDate">Дата рождения</label>
                <input type="date" id="birthDate" v-model="form.birthDate" disabled />
            </div>
            <div class="form-group">
                <label for="gender">Пол</label>
                <select id="gender" v-model="form.gender" required>
                    <option value="male">Мужской</option>
                    <option value="female">Женский</option>
                </select>
            </div>
            <div class="form-group">
                <label for="graduationYear">Год окончания обучения в школе</label>
                <input type="number" id="graduationYear" v-model="form.graduationYear" required />
            </div>
            <div class="form-group">
                <label for="faculty">Факультет</label>
                <select id="faculty" v-model="form.faculty" required>
                    <option value="faculty1">Факультет 1</option>
                    <option value="faculty2">Факультет 2</option>
                </select>
            </div>
            <div class="form-group">
                <label for="email">Электронная почта для связи</label>
                <input type="email" id="email" v-model="form.email" required />
            </div>
            <div class="form-group">
                <label for="phone">Мобильный телефон</label>
                <input type="tel" id="phone" v-model="form.phone" required />
            </div>
            <button type="submit">Отправить</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                lastName: '',
                firstName: '',
                middleName: '',
                birthDate: '',
                gender: '',
                graduationYear: '',
                faculty: '',
                email: '',
                phone: '',
            },
            submitted: false,
        };
    },
    created() {
        // Инициализация формы с данными пользователя
        this.form.lastName = 'Иванов';
        this.form.firstName = 'Иван';
        this.form.middleName = 'Иванович';
        this.form.birthDate = '2000-01-01';
        this.form.email = 'ivanov@example.com';
    },
    methods: {
        submitApplication() {

        },
        editApplication() {

        },
    },
};
</script>

<style scoped>
.error {
    color: red;
}


.main-container {
    background-color: white;
    color: #3C388D;
    padding: 20px;
    font-family: Arial, sans-serif;
}

h1 {
    font-family: "NekstRegular", "Verdana", sans-serif;
    font-size: 2em;
    text-align: center;
    margin-bottom: 0.5em;
}

.info-text {
    font-family: "NekstRegular", "Verdana", sans-serif;
    color: #5F5F5F;
    margin-bottom: 2em;
}

.form-container {
    width: 50%;
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

textarea {
    height: 8em;
}

button {
    padding: 0.5em;
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