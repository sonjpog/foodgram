
from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Настройки отображения и управления тегами в админ-панели."""

    list_display = ('id', 'name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('name',)}
