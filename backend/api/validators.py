from rest_framework.exceptions import ValidationError

from .models import Subscription


def validate_not_self_subscription(user, subscribed_user):
    """Проверка, что пользователь не пытается подписаться на себя"""
    if user == subscribed_user:
        raise ValidationError('Вы не можете подписаться на себя!')


def validate_already_subscribed(user, subscribed_user):
    """Проверка, что пользователь уже подписан на другого пользователя"""
    if Subscription.objects.filter(
        user=user, subscribed_user=subscribed_user
    ).exists():
        raise ValidationError(
            'Вы уже подписаны на данного пользователя!'
        )
