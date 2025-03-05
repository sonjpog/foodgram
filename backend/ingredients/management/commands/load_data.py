import json
from pathlib import Path

from django.core.management.base import BaseCommand
from ingredients.models import Ingredient
from tags.models import Tag


class Command(BaseCommand):
    help = 'Загрузить данные в модель ингредиентов и тегов'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Старт команды'))
        base_dir = Path(__file__).resolve().parents[3]
        data_dir = base_dir / 'data'
        ingredients_file = data_dir / 'ingredients.json'

        if not ingredients_file.exists():
            self.stdout.write(
                self.style.ERROR(f'Файл {ingredients_file} не найден')
            )
            return

        with ingredients_file.open(encoding='utf-8') as data_file_ingredients:
            ingredient_data = json.load(data_file_ingredients)
            for ingredient in ingredient_data:
                Ingredient.objects.get_or_create(**ingredient)

        self.stdout.write(self.style.SUCCESS('Ингредиенты загружены'))
        tags_file = data_dir / 'tags.json'

        if not tags_file.exists():
            self.stdout.write(self.style.ERROR(f'Файл {tags_file} не найден'))
            return

        with tags_file.open(encoding='utf-8') as data_file_tags:
            tags_data = json.load(data_file_tags)
            for tag in tags_data:
                Tag.objects.get_or_create(**tag)

        self.stdout.write(self.style.SUCCESS('Теги загружены'))
