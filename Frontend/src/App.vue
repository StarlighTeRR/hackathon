<template>
  <div class="header">
    <nav className="header__container">
      <div className="right-link">
        <div class="header__button">
          <RouterLink to="/login">Войти</RouterLink>
        </div>
      </div>

      <div className="right-link">
        <label for="dropdown-checkbox" className="profile__header">
          <span className="dropdown-text">Мой профиль</span>
          <span className="dropdown__arrow"></span>
        </label>
        <input type="checkbox" id="dropdown-checkbox" className="dropdown-checkbox">
        <div className="dropdown-menu">
          <ul>
            <li className="dropdown-item dropdown-text" @click="OpenUserProfilePage">Профиль</li>
            <li className="dropdown-item dropdown-text" @click="OpenQuestionnairePage">Моя анкета</li>
            <li className="dropdown-item dropdown-text">Выйти</li>
          </ul>
        </div>
      </div>
    </nav>
  </div>

  <div class="subtop">
    <div class="header__container">
      <div class="header-block">
        <div class="logotype-block">
          <span>
            <p>Абитуриентам</p>
          </span>
        </div>
      </div>
    </div>
  </div>

  <div class="header-nav">
    <div class="header__container">
      <div class="row">
        <div class="col-xs-12">
          <ul class="nav-menu">
            <li class="dropdown dropdown--white active" @click="OpenHomePage">Выбор факультета</li>
            <li class="dropdown dropdown-cabinet" @click="OpenUserProfilePage">Личный кабинет
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <main>
    <RouterView />
  </main>
</template>

<script>
import router from './router';

export default {
  data() {
    return {
      login: '',
      password: ''
    };
  },
  methods: {
    OpenUserProfilePage() {
      router.push('UserProfile')
    },
    OpenQuestionnairePage() {
      router.push({ name: 'questionnaire' })
    }
    ,
    OpenHomePage() {
      router.push({ name: 'home' })
    }
  }
};
</script>

<style>
body {
  font-family: "NekstRegular", "Verdana", sans-serif;
  margin: 0;
}

nav {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.header__container a {
  color: white;
  text-decoration: none;
  margin: 0 10px;
}

.header__button,
.header__button a {
  display: flex;
  color: #3C388D;
  cursor: pointer;
  padding: 0 15px;
  font-size: 15px;
  line-height: 1.5;
  height: 44px;
  overflow-y: hidden;
  justify-content: center;
  align-items: center;
}

.right-link:hover {
  background-color: #f9f9f9;
}

.header__container {
  margin: 0 auto;
  max-width: 1170px;
}

.header {
  background-color: #ECECF4;
  height: 44px;
}

.header-nav {
  background-color: #3c388d;
  height: 41px;
}

/* Стили для ссылок */
a.right-link {
  margin-left: auto;
  margin-right: 10px;
}

.right-link {
  position: relative;
  width: max-content;
  border-radius: 5px;
}

.active {
  background-color: #9fc53a;
}

li {
  list-style-type: none;
}

.profile__header {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 0px 15px;
  font-size: 15px;
  line-height: 1.5;
  height: 44px;
}

.dropdown {
  float: left;
  padding: 11px 15px;
}

.dropdown--white {
  color: white;
}

.dropdown-cabinet {
  color: white;
}

.dropdown:hover {
  color: black;
  background-color: white;
  cursor: pointer;
}

.dropdown:first-child {
  margin-left: -41px;
}

.dropdown__arrow {
  transition: all 0.3s;
  transform: scale(1) rotate(0deg);
  margin: auto 0 auto 10px;
  background: url(assets/dropdown-arrow.svg);
  width: 16px;
  height: 10px;
  display: inline-block;
  position: relative;
}

.dropdown-checkbox {
  display: none;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 1px);
  left: 0;
  width: 100%;
  display: none;
  border: 1px solid #ccc;
  border-top: none;
  background-color: #fff;
  z-index: 1000;
}

.dropdown-menu ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.dropdown-menu li {
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.dropdown-menu li:hover {
  background-color: #f1f1f1;
}

.dropdown-text {
  color: #3C388D
}

.dropdown-item {
  cursor: pointer;
  text-align: left;
}

.dropdown-checkbox:checked~.dropdown-menu {
  display: block;
}

.dropdown-checkbox:checked~.dropdown__arrow {
  transition: all 0.3s;
  transform: scale(0) rotate(-180deg);
}
</style>