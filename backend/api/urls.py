from api.views import (
    BaseAPIRootView,
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet,
    CustomUserViewSet,
    short_url
)

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"


class RuDefaultRouter(DefaultRouter):
    """Показывает описание главной страницы API на русском языке."""

    APIRootView = BaseAPIRootView


router = RuDefaultRouter()
router.register("tags", TagViewSet, "tags")
router.register("ingredients", IngredientViewSet, "ingredients")
router.register("recipes", RecipeViewSet, "recipes")
router.register("users", CustomUserViewSet, "users")

urlpatterns = (
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path("auth/", include("djoser.urls.authtoken")),
    path('recipes/<int:pk>/short-url/', short_url, name='short_url'),
)
