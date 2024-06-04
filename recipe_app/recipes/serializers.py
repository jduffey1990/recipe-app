# serializers.py
from rest_framework import serializers
from .models import Recipe, RecipeIngredient

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'name', 'quantity', 'unit', 'recipe'] 

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients']  # Ensure id is included
