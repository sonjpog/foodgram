import json
import os

from django.core.management.base import BaseCommand

from ingredients.models import Ingredient
from tags.models import Tag


class Command(BaseCommand):
    help = 'Загрузить данные в модель ингредиентов и тегов'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Старт команды'))
        base_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "../../../.."))
        data_dir = os.path.join(base_dir, 'data')
        ingredients_file = os.path.join(data_dir, 'ingredients.json')
        if not os.path.exists(ingredients_file):
            self.stdout.write(self.style.ERROR(
                f'Файл {ingredients_file} не найден'))
            return

        with open(ingredients_file, encoding='utf-8') as data_file_ingredients:
            ingredient_data = json.load(data_file_ingredients)
            for ingredient in ingredient_data:
                Ingredient.objects.get_or_create(**ingredient)

        self.stdout.write(self.style.SUCCESS('Ингредиенты загружены'))
        tags_file = os.path.join(data_dir, 'tags.json')
        if not os.path.exists(tags_file):
            self.stdout.write(self.style.ERROR(f'Файл {tags_file} не найден'))
            return

        with open(tags_file, encoding='utf-8') as data_file_tags:
            tags_data = json.load(data_file_tags)
            for tag in tags_data:
                Tag.objects.get_or_create(**tag)

        self.stdout.write(self.style.SUCCESS('Теги загружены'))
