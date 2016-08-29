import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import App from './App'
import Dogs from './components/Dogs'
import About from './components/About'
import Home from './components/Home'

// install router
Vue.use(Router)
Vue.use(VueResource)

// routing
var router = new Router()

router.map({
  '/dogs': {
    component: Dogs
  },
  '/about': {
    component: About
  },
  '/home': {
    component: Home
  }
})

router.start(App, '#app')
