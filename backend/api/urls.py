from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CustomUserViewSet, IngredientViewSet, RecipeViewSet,
                       TagViewSet, short_url)

app_name = 'api'

router = DefaultRouter()

router.register('tags', TagViewSet, 'tags')
router.register('ingredients', IngredientViewSet, 'ingredients')
router.register('recipes', RecipeViewSet, 'recipes')
router.register('users', CustomUserViewSet, 'users')

urlpatterns = (
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.authtoken')),
    path('recipes/<int:pk>/short-url/', short_url, name='short_url'),
)
