<template>
  <div class="container">
    <h1>Recipes</h1>
    <ul class="recipe-list">
      <li v-for="recipe in recipes" :key="recipe.id" class="recipe-item">
        <div class="recipe-header">
          <h2>{{ recipe.title }}</h2>
          <p>{{ recipe.description }}</p>
        </div>
        <img :src="recipe.photo" alt="Recipe photo" v-if="recipe.photo" class="recipe-photo"/>
        <ul class="ingredient-list">
          <li v-for="ingredient in recipe.ingredients" :key="ingredient.name" class="ingredient-item">
            {{ ingredient.quantity }} {{ ingredient.unit }} of {{ ingredient.name }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      recipes: []
    };
  },
  created() {
    this.fetchRecipes();
  },
  methods: {
    async fetchRecipes() {
      try {
        const response = await axios.get('http://localhost:8000/api/recipes/');
        const recipes = await Promise.all(response.data.map(async recipe => {
          const ingredientsResponse = await axios.get(`http://localhost:8000/api/ingredients/?recipe=${recipe.id}`);
          recipe.ingredients = ingredientsResponse.data;
          return recipe;
        }));
        this.recipes = recipes;
      } catch (error) {
        console.error('Error fetching recipes:', error);
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.recipe-list {
  list-style: none;
  padding: 0;
}

.recipe-item {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.recipe-header {
  margin-bottom: 10px;
}

.recipe-header h2 {
  margin: 0;
  color: #42b983;
}

.recipe-header p {
  margin: 5px 0 0;
  color: #666;
}

.recipe-photo {
  max-width: 100%;
  border-radius: 10px;
  margin: 10px 0;
}

.ingredient-list {
  list-style: none;
  padding: 0;
  margin: 10px 0 0;
}

.ingredient-item {
  background-color: #f2f2f2;
  border-radius: 5px;
  padding: 5px;
  margin-bottom: 5px;
  color: #333;
}
</style>
