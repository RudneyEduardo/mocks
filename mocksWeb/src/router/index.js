import Vue from 'vue'
import VueRouter from 'vue-router'
import Container from '../components/Container.vue'
import PhoneConsentimento from '../components/PhoneConsentimento.vue'
import PhoneGetAPay from '../components/PhoneGetAPay.vue'

Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    name:'Container',
    component: Container

  },
  {
    path:'/phoneConsentimento/:From',
    name: 'PhoneConsentimento',
    component: PhoneConsentimento
  },
  {
    path:'/phoneGetAPay/:From',
    name:'PhoneGetAPay',
    component: PhoneGetAPay
  }
  ]

const router = new VueRouter({
  routes
})

export default router
