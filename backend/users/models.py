from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from foodgram import constants


class User(AbstractUser):
    """Модель пользователя."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=constants.MAX_FIRST_NAME_LENGTH
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=constants.MAX_LAST_NAME_LENGTH
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=constants.MAX_EMAIL_LENGTH,
        unique=True,
        db_index=True
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=constants.MAX_USERNAME_LENGTH,
        unique=True,
        validators=[RegexValidator(constants.REGULAR_CHECK_LOGIN_VALID)]
    )
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @classmethod
    def normalize_email(cls, email: str) -> str:
        """Normalize the email address by lowercasing the domain part of it."""
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name.lower() + '@' + domain_part.lower()
        return email


class Subscription(models.Model):
    """Модель подписки на авторов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='subscriptions'
    )
    subscribed_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='subscribers'
    )

    class Meta:
        ordering = ('user', 'subscribed_user')
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'subscribed_user'],
                name='unique_user_subscription'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return (
            f'{self.user.username} подписан на '
            f'{self.subscribed_user.username}'
        )
