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
    list_display_links = ('email',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Подписки пользователя."""

    list_display = ('user', 'subscribed_user')
    list_display_links = ('user', 'subscribed_user')
    list_filter = ('user',)
    search_fields = ('user__email', 'subscribed_user__email')

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related('user', 'subscribed_user')
        )
