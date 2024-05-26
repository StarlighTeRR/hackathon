import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
      alias: '/'
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/userprofile',
      name: 'userprofile',
      component: () => import('../views/UserProfileView.vue')
    },
    {
      path: '/questionnaire',
      name: 'questionnaire',
      component: () => import('../views/QuestionnaireView.vue')
    }
  ]
})


router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;

  if ((to.name === 'login' || to.name === 'register') && isAuthenticated) {
    // Если пользователь авторизован и пытается попасть на страницы login или register, перенаправьте его на userprofile
    next({ name: 'userprofile' });
  } 
  else if (( to.name === 'userprofile') && !isAuthenticated) {
    // Если пользователь авторизован и пытается попасть на страницы login или register, перенаправьте его на userprofile
    next({ name: 'home' });
  }
  else {
    next(); // В противном случае разрешите навигацию
  }
});

//  Защита навигации по авторизации
export default router
