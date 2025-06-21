import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Register from '../views/Register.vue'
import ActivateEmail from '../views/ActivateEmail.vue'
import Login from '../views/Login.vue'
import ChangePassword from '../views/ChangePassword.vue'  
import Personal from '../views/Personal.vue'
import Collect from '../views/Collect.vue'
import MemberCard from '../views/MemberCard.vue'
import Orders from '../views/Orders.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/movie/:id',
    name:'MovieDetail',
    component:MovieDetail
  },
  {
    path:'/register',
    name:'Register',
    component:Register
  },
  {
    path:'/login',
    name:'Login',
    component:Login
  },
  {
    path:'/change_password',
    name:'ChangePassword',
    component:ChangePassword,
    meta: {
      requiresLogin: true
    }
  },
  {
    path:'/personal',
    name:'Personal',
    component:Personal,
    meta: {
      requiresLogin: true
    }
  },
  {
    path:'/collect',
    name:'Collect',
    component:Collect,
    meta: {
      requiresLogin: true
    }
  },
  {
    path:'/member_card',
    name:'MemberCard',
    component:MemberCard,
  },
  {
    path:'/orders',
    name:'Orders',
    component:Orders,
    meta: {
      requiresLogin: true
    }
  },
  {
    path:'/activate/:uid/:token',
    name:'ActivateEmail',
    component:ActivateEmail,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// 路由导航守卫
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.state.isLogin;
  if (isLoggedIn && (to.name === 'Login' || to.name === 'Register')) {
    next({ name: 'home' });
  }
  else if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!isLoggedIn) {
      next({ name: 'Login', query: { jump: to.path } });
    } else {
      next();
    }
  } else {
    next();
  }
})
export default router
