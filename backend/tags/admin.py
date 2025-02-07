
from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Настройки отображения и управления тегами в админ-панели."""
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    ordering = ('id',)
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Tag
