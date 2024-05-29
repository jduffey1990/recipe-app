from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import RecipeViewSet, RecipeIngredientViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', RecipeIngredientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

