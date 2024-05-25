<template>
    <section className="sign">
        <div className="container">
            <div className="sign-content">
                <div className="sign-form">
                    <h2 className="form-title">Вход</h2>
                    <form className="register-form" @submit.prevent="goToRegistration">
                        <div className="form-group">
                            <input type="email" v-model="login" placeholder="Логин (email)">
                        </div>
                        <div className="form-group">
                            <input type="password" v-model="password" placeholder="Пароль">
                        </div>
                        <div className="form-container">
                            <div className="form-group form-button">
                                <input type="submit" @click="Authentificate" className="form-submit" value="Войти">
                            </div>
                            <div className="form-button">
                                <button type="button" className="form-submit"
                                    @click="$router.push({ name: 'register' })">Регистрация</button>
                            </div>
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
            password: ''
        };
    },
    methods: {
        Authentificate() {
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
    /* Flex-grow property to make both elements take equal space */
    margin-right: 10px;
    /* Add some spacing between the elements */
}

.form-group:last-child,
.form-button:last-child {
    margin-right: 0;
    /* Remove the margin on the last element */
}

.form-submit {
    width: 100%;
    /* Ensure the input/button takes the full width of the parent */
}

.form-group,
.form-button {
    flex: 1;
    /* Flex-grow property to make both elements take equal space */
    margin-right: 10px;
    /* Add some spacing between the elements */
    margin-bottom: 15px;
}

.form-group:last-child,
.form-button:last-child {
    margin-right: 0;
    /* Remove the margin on the last element */
}

.form-submit {
    width: 100%;
    /* Ensure the input/button takes the full width of the parent */
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
</style>
