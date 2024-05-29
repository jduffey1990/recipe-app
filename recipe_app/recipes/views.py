from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe, RecipeIngredient
from .serializers import RecipeSerializer, RecipeIngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().prefetch_related('ingredients')
    serializer_class = RecipeSerializer

    @action(detail=False, methods=['delete'], url_path='delete_by_recipe')
    def delete_recipe(self, request):
        recipe_id = request.query_params.get('id', None)
        if recipe_id:
            try:
                recipe = Recipe.objects.get(id=recipe_id)
                recipe.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Recipe.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

    @action(detail=False, methods=['delete'], url_path='delete_by_recipe')
    def delete_recipe_ingredients(self, request):
        recipe_id = request.query_params.get('recipe_id', None)
        if recipe_id:
            ingredients = RecipeIngredient.objects.filter(recipe_id=recipe_id)
            if ingredients.exists():
                ingredients.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
