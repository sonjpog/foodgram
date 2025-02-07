from django.db import models

from foodgram.constants import (MAX_INGREDIENT_NAME_LENGTH,
                                MAX_MEASUREMENT_LENGTH)


class Ingredient(models.Model):
    """Модель для хранения ингредиентов."""
    name = models.CharField(
        'Название',
        max_length=MAX_INGREDIENT_NAME_LENGTH,
        unique=True
    )
    measurement_unit = models.CharField(
        max_length=MAX_MEASUREMENT_LENGTH
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']

    def __str__(self):
        return self.name
