from django.db import models

from foodgram.constants import MAX_TAG_LENGTH


class Tag(models.Model):
    """Модель для хранения тегов."""

    name = models.CharField(
        'Название',
        max_length=MAX_TAG_LENGTH,
        unique=True
    )
    slug = models.SlugField(
        'Слаг',
        max_length=MAX_TAG_LENGTH,
        unique=True,
        blank=True,
        help_text='Короткое уникальное название для URL.'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name
