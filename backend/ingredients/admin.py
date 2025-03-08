from django.contrib import admin

from .models import Ingredient


@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    """Ингредиенты."""

    list_display = ('name', 'measurement_unit')
    search_fields = ['name']
