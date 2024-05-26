<template>
  <div class="header" @click="handleClickOutside">
    <nav class="header__container">
      <div v-if="!isAuthenticated" class="right-link">
        <div class="header__button">
          <RouterLink to="/login">Войти</RouterLink>
        </div>
      </div>

      <div v-else class="right-link" ref="dropdown">
        <label for="dropdown-checkbox" class="profile__header">
          <span class="dropdown-text">Мой профиль</span>
          <span class="dropdown__arrow" :class="{ rotated: isDropdownOpen }"></span>
        </label>
        <input type="checkbox" id="dropdown-checkbox" class="dropdown-checkbox" v-model="isDropdownOpen">
        <div class="dropdown-menu">
          <ul>
            <li class="dropdown-item dropdown-text" @click="OpenUserProfilePage">Профиль</li>
            <li class="dropdown-item dropdown-text" @click="OpenQuestionnairePage">Моя анкета</li>
            <li class="dropdown-item dropdown-text" @click="logout">Выйти</li>
          </ul>
        </div>
      </div>
    </nav>
  </div>

  <div class="subtop">
    <div class="subtop__container">
      <div class="header-block">
        <div class="logotype-block" p style="padding: 15px;">
          <div class="logo-hackathon"></div>
          <div class="divider"></div>
        </div>
        <span>
          <p>{{ currentPageTitle }}</p>
        </span>
      </div>
    </div>
  </div>

  <div class="header-nav">
    <div class="header__container">
      <div class="row">
        <div class="col-xs-12">
          <ul class="nav-menu">
            <li class="dropdown dropdown--white" :class="{ active: currentPage === 'home' }" @click="OpenHomePage">Выбор факультета</li>
            <li class="dropdown dropdown-cabinet" :class="{ active: currentPage === 'UserProfile' }" @click="OpenUserProfilePage">Личный кабинет</li>
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
import { mapActions, mapGetters } from 'vuex';
import router from './router';

export default {
  computed: {
    ...mapGetters({
      isAuthenticated: 'isAuthenticated', // Получаем isAuthenticated из геттеров Vuex
    }),
  },
  data() {
    return {
      login: '',
      password: '',
      currentPageTitle: 'Абитуриентам',
      isDropdownOpen: false,
      activeMenuItem: 'home'
    };
  },
  watch: {
    $route(to, from) {
      this.updatePageTitle(to);
      this.isDropdownOpen = false;
    }
  },
  methods: {
    ...mapActions(['removeAuthToken']),
    logout() {
      this.removeAuthToken();
      this.$router.push({ name: 'login' });
    },
    OpenUserProfilePage() {
    router.push('UserProfile');
    this.currentPage = 'UserProfile';
    },
    OpenQuestionnairePage() {
      router.push({ name: 'questionnaire' });
      this.currentPage = 'null';
    },
    OpenHomePage() {
    router.push({ name: 'home' });
    this.currentPage = 'home';
    },
    updatePageTitle(route) 
    {

  switch (route.name) {
    case 'home':
      this.currentPageTitle = 'Выбор факультета';
      break;
    case 'UserProfile':
      this.currentPageTitle = 'Профиль пользователя';
      break;
    case 'questionnaire':
      this.currentPageTitle = 'Моя анкета';
      break;
    case 'login':
      this.currentPageTitle = 'Вход';
      this.currentPage = 'null';
      break;
    case 'register':
      this.currentPageTitle = 'Регистрация';
      this.currentPage = 'null';
      break;
    default:
      this.currentPageTitle = 'Личный кабинет';
      break;
      }
    },
    handleClickOutside(event) {
      const dropdown = this.$refs.dropdown;
      if (dropdown && !dropdown.contains(event.target)) {
        this.isDropdownOpen = false;
      }
    }
  },
  mounted() {
  this.updatePageTitle(this.$route);
  this.currentPage = this.$route.name;
  document.addEventListener('click', this.handleClickOutside);
  this.OpenHomePage();
  },
  beforeDestroy() {
    document.removeEventListener('click', this.handleClickOutside);
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
  justify-content: right;
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

a.right-link {
  margin-left: auto;
  margin-right: 10px
  r
}

.right-link {
  position: relative;
  width: max-content;
  text-align: right;
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
  background: url(assets/dropdown-arrow.svg);
  margin: auto 0 auto 10px;
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

.subtop {
  background-color: white;
  display: flex;
  justify-content: flex-start;
}

.subtop__container {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  margin: 0 auto;
  max-width: 1170px;
}

.header-block {
  display: flex;
  align-items: center;
}

.logotype-block {
  display: flex;
  align-items: center;
}

.logo-hackathon {
  margin: 0 10px 0 0;
  background: url('assets/logo_hackathon.svg');
  background-size: contain;
  width: 75px;
  height: 75px;
}

.divider {
  width: 2px;
  height: 60px;
  background-color: #3C388D;
  margin: 0 10px;
}

span {
  display: flex;
  align-items: center;
}
</style>