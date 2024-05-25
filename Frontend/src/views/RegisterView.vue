<template>
    <section className="sign">
        <div className="container">
            <div className="sign-content">
                <div className="sign-form">
                    <h2 className="form-title">Регистрация</h2>
                    <form className="register-form" @submit.prevent="registrate">
                        <div className="form-group">
                            <input type="email" v-model="login" placeholder="Логин (e-mail)">
                        </div>
                        <div className="form-group">
                            <input type="text" v-model="surname" placeholder="Фамилия" />
                        </div>
                        <div className="form-group">
                            <input type="text" v-model="name" placeholder="Имя" />
                        </div>
                        <div className="form-group">
                            <input type="text" v-model="patronymic" placeholder="Отчество" />
                        </div>
                        <div className="form-group">
                            <input type="date" v-model="birthdate" placeholder="Дата рождения" />
                        </div>
                        <div className="form-group">
                            <input type="password" v-model="pass" placeholder="Пароль" />
                        </div>
                        <div className="form-group">
                            <input type="password" v-model="re_pass" placeholder="Подтверждение пароля" />
                        </div>
                        <div className="form-group form-button">
                            <input type="submit" name="sign" id="sign" className="form-submit"
                                value="Зарегистрироваться" />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    data() {
        return {
            login: '',
            name: '',
            surname: '',
            patronymic: '',
            birthDate: '',
            password: '',
            confirmPassword: ''
        };
    },
    methods: {
        async registrate() {
            console.log(this.login, this.name, this.surname, this.patronymic, this.birthDate, this.password, this.confirmPassword)
            // Логика регистрации RESTAPI
            // Пример: axios.post('/api/register', this.registerForm)
            // .then(response => {
            //   this.$router.push('/profile');
            // });
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

/* Иконки внутри формы */
.form-group i {
    position: absolute;
    top: 50%;
    left: 10px;
    transform: translateY(-50%);
    color: #333;
}
</style>