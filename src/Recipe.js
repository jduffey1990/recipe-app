import React from "react";
import RecipeData from "./RecipeData.js"

function Recipe({ recipe, deleteRecipe }) {

  //This component is made to set up the tablke format for one given recipe.

  return (
    <tr>
      <td>{recipe.name}</td>
      <td>{recipe.cuisine}</td>
      <td>
        <img src={recipe.photo} alt={recipe.name} />
      </td>
      <td className="content_td"><p>{recipe.ingredients}</p></td>
      <td className="content_td"><p>{recipe.preparation}</p></td>
      <td>
        <button name="delete" onClick={deleteRecipe}>Delete</button>
      </td>
    </tr>
  );
}

export default Recipe;