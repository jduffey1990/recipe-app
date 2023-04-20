import React from "react";
import Recipe from "./Recipe.js"

function RecipeList({ recipes, deleteRecipe }) {



  return (
    <table>
      <thead>
        <tr> //header where the titles of the columns go
          <th>Name</th>
          <th>Cuisine</th>
          <th>Photo</th>
          <th>Ingredients</th>
          <th>Preparations</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody> //we are now going to map over the recipes, also delivering the prop to the Recipe component.
        {recipes.map((recipe, index) => (
          <Recipe
            deleteRecipe={() => deleteRecipe(index)}
            key={index}
            recipe={recipe}
          />
        ))}
      </tbody>
    </table>
  );
}

export default RecipeList;
