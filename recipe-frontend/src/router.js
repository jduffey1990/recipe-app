import Vue from 'vue'
import Router from 'vue-router'
import CreateRecipe from './components/CreateRecipe.vue'
import RecipeList from './components/RecipeList.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',  // Ensures clean URLs
  routes: [
    {
      path: '/',
      name: 'CreateRecipe',
      component: CreateRecipe
    },
    {
      path: '/recipes',
      name: 'RecipeList',
      component: RecipeList
    }
  ]
})