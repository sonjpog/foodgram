from django.contrib import admin

from .models import Favorite, Recipe, RecipeIngredient, ShoppingCart


class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Рецепты."""

    list_display = ('name', 'author')
    list_display_links = ('name', 'author')
    search_fields = ('name', 'author__username')
    list_filter = ('tags',)
    ordering = ('-id',)
    inlines = RecipeIngredientInline,
    filter_horizontal = ('tags', 'ingredients')

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related('author')
            .prefetch_related('tags', 'ingredients')
        )


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    """Ингредиенты рецепта."""

    list_display = ('recipe', 'ingredient', 'amount')
    list_display_links = ('recipe', 'ingredient')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Список покупок."""

    list_display = ('user', 'recipe')
    list_display_links = ('user', 'recipe')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Избранные рецепты."""

    list_display = ('user', 'recipe', 'created_at')
    list_display_links = ('user', 'recipe')
