from django_filters.rest_framework import FilterSet, filters
from rest_framework.exceptions import ValidationError

from ingredients.models import Ingredient
from recipes.models import Recipe
from tags.models import Tag


class IngredientFilter(FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
        label='Tags'
    )
    is_favorited = filters.BooleanFilter(method='boolean_filter',
                                         field_name='favorited_by')
    is_in_shopping_cart = filters.BooleanFilter(
        method='boolean_filter',
        field_name='in_shopping_cart')

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')

    def boolean_filter(self, queryset, name, value):
        if self.request.user.is_anonymous:
            raise ValidationError('Чтобы посмотреть избранное, нужено зарегистрироваться!')
        if value:
            return queryset.filter(**{f'{name}__user': self.request.user})

        else:
            return queryset.exclude(**{f'{name}__user': self.request.user})

