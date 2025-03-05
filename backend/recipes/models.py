from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ingredients.models import Ingredient
from tags.models import Tag

from foodgram import constants

User = get_user_model()


class Recipe(models.Model):
    """Модель для хранения рецептов."""
    name = models.CharField(
        'Название', max_length=constants.MAX_FIELD_LENGTH
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    image = models.ImageField('Изображение', upload_to='recipes/')
    text = models.TextField('Описание')
    cooking_time = models.PositiveIntegerField(
        'Время приготовления (мин)',
        validators=[
            MinValueValidator(
                constants.MIN_COOKING_TIME,
                message=(
                    f'Время приготовления не может быть меньше '
                    f'{constants.MIN_COOKING_TIME} минут.'
                )
            ),
            MaxValueValidator(
                constants.MAX_COOKING_TIME,
                message=(
                    f'Время приготовления не может превышать '
                    f'{constants.MAX_COOKING_TIME} минут.'
                )
            )
        ]
    )
    tags = models.ManyToManyField(
        Tag, related_name='recipes', verbose_name='Теги'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    favorite = models.ManyToManyField(
        User,
        through='Favorite',
        related_name='favorite_recipes',
        blank=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Модель количества ингредиентов в рецепте."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='in_recipes',
        verbose_name='Ингредиент'
    )
    amount = models.PositiveIntegerField(
        'Количество',
        validators=[
            MinValueValidator(
                constants.AMOUNT_MIN,
                message=(
                    f'Количество не может быть меньше {constants.AMOUNT_MIN}.'
                )
            ),
            MaxValueValidator(
                constants.AMOUNT_MAX,
                message=(
                    f'Количество не может превышать {constants.AMOUNT_MAX}.'
                )
            )
        ]
    )

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецепта'
        ordering = ['ingredient__name']

    def __str__(self):
        return f'{self.ingredient.name} в {self.recipe.name}'


class ShoppingCart(models.Model):
    """Модель списка покупок пользователя."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='in_shopping_cart',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'
        ordering = ['user', 'recipe']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_recipe_in_cart'
            )
        ]

    def __str__(self):
        return (
            f'{self.recipe.name} в списке покупок у {self.user.username}'
        )


class Favorite(models.Model):
    """Модель избранных рецептов пользователя."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorited_by',
        verbose_name='Рецепт'
    )
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные рецепты'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorite'
            )
        ]

    def __str__(self):
        return (
            f'{self.user.username} добавил в избранное {self.recipe.name}'
        )
