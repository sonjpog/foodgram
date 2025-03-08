from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Subscription, User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """Пользовательский админ."""

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'avatar'
    )
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Подписки пользователя."""

    list_display = ('user', 'subscribed_user')
    list_filter = ('user',)
    search_fields = ('user__email', 'subscribed_user__email')
