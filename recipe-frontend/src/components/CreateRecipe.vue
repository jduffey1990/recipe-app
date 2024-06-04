<template>
  <div class="container">
    <h1>Create Recipe</h1>
    <form @submit.prevent="createRecipe">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" v-model="recipe.title" id="title" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea v-model="recipe.description" id="description" required></textarea>
      </div>
      <div class="form-group">
        <h3>Ingredients</h3>
        <div v-for="(ingredient, index) in recipe.ingredients" :key="index" class="ingredient-group">
          <input type="text" v-model="ingredient.name" placeholder="Ingredient name" required>
          <input type="number" v-model="ingredient.quantity" placeholder="Quantity" required>
          <select v-model="ingredient.unit" placeholder="Unit" required>
            <option v-for="unit in units" :key="unit.value" :value="unit.value">
              {{ unit.text }}
            </option>
          </select>
          <button type="button" @click="removeIngredient(index)" class="remove-btn">Remove</button>
        </div>
        <button type="button" @click="addIngredient" class="add-btn">Add Ingredient</button>
      </div>
      <button type="submit" class="submit-btn">Create Recipe</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      recipe: {
        title: '',
        description: '',
        ingredients: [],
      },
      units: [
        { "value": "ml", "text": "Milliliters" },
        { "value": "l", "text": "Liters" },
        { "value": "tsp", "text": "Teaspoons" },
        { "value": "tbsp", "text": "Tablespoons" },
        { "value": "fl oz", "text": "Fluid Ounces" },
        { "value": "cup", "text": "Cups" },
        { "value": "pt", "text": "Pints" },
        { "value": "qt", "text": "Quarts" },
        { "value": "gal", "text": "Gallons" },
        { "value": "mg", "text": "Milligrams" },
        { "value": "g", "text": "Grams" },
        { "value": "kg", "text": "Kilograms" },
        { "value": "oz", "text": "Ounces" },
        { "value": "lb", "text": "Pounds" },
        { "value": "pinch", "text": "Pinches" },
        { "value": "dash", "text": "Dashes" },
        { "value": "smidgen", "text": "Smidgens" },
        { "value": "clove", "text": "Clove" },
        { "value": "dl", "text": "Deciliters" },
        { "value": "hl", "text": "Hectoliters" },
        { "value": "piece", "text": "Pieces" },
        { "value": "stick", "text": "Sticks" },
        { "value": "sheet", "text": "Sheets" },
        { "value": "can", "text": "Cans" },
        { "value": "jar", "text": "Jars" },
        { "value": "pkg", "text": "Packages" },
        { "value": "bunch", "text": "Bunches" },
        { "value": "bag", "text": "Bags" },
        { "value": "bottle", "text": "Bottles" },
        { "value": "sprig", "text": "Sprigs" },
        { "value": "head", "text": "Heads" },
        { "value": "slice", "text": "Slices" },
        { "value": "grain", "text": "Grains" },
        { "value": "drop", "text": "Drops" },
        { "value": "whole", "text": "Whole" },
      ]
    };
  },
  methods: {
    addIngredient() {
      this.recipe.ingredients.push({ name: '', quantity: '', unit: '' });
    },
    removeIngredient(index) {
      this.recipe.ingredients.splice(index, 1);
    },
    onFileChange(event) {
      this.recipe.photo = event.target.files[0];
    },
    async createRecipe() {
      const formData = new FormData();
      formData.append('title', this.recipe.title);
      formData.append('description', this.recipe.description);

      try {
        const baseURL = process.env.VUE_APP_API_URL || 'http://localhost:8000';

        const response = await axios.post(`${baseURL}/api/recipes/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        const recipeId = response.data.id;

        for (const ingredient of this.recipe.ingredients) {
          const ingredientData = new FormData();
          ingredientData.append('recipe', recipeId);
          ingredientData.append('name', ingredient.name);
          ingredientData.append('quantity', ingredient.quantity);
          ingredientData.append('unit', ingredient.unit);

          const baseURL = process.env.VUE_APP_API_URL || 'http://localhost:8000';
          
          await axios.post(`${baseURL}/api/ingredients/`, ingredientData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
        }

        this.$router.push('/recipes');
      } catch (error) {
        console.error('Error response:', error.response);
        if (error.response) {
          console.error('Data:', error.response.data);
          console.error('Status:', error.response.status);
          console.error('Headers:', error.response.headers);
        } else if (error.request) {
          console.error('Request:', error.request);
        } else {
          console.error('Message:', error.message);
        }
      }
    }
  }
};
</script>


<style>
.container {
  max-width: 600px;
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

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
  font-size: 16px;
  color: #333;
}

.ingredient-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.ingredient-group input,
.ingredient-group select {
  margin-right: 10px;
  flex: 1;
}

.remove-btn,
.add-btn,
.submit-btn {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.remove-btn {
  background-color: #e74c3c;
}

.remove-btn:hover,
.add-btn:hover,
.submit-btn:hover {
  background-color: #369f6e;
}

.remove-btn:hover {
  background-color: #c0392b;
}
</style>
