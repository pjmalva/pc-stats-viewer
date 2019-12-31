import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'site-home',
      component: () => import('./../views/Site/Home.vue'),
    },

    {
      path: '/admin/',
      name: 'admin',
      component: () => import('./../views/Admin/Home.vue'),
      meta: {    requiresAuth: true   }
    },

    {
      path: '/login',
      name: 'login',
      component: () => import('./../views/Admin/Auth/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./../views/Admin/Auth/Register.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('./../views/Admin/Auth/Logout.vue'),
      meta: {    requiresAuth: true   }
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!localStorage.getItem('token')) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
