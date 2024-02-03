from django_filters import FilterSet, ModelChoiceFilter, CharFilter
from .models import Article

TYPE = (
        ('tank', 'Танк'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )


class ArticleFilter(FilterSet):
    category = ModelChoiceFilter(field_name='category__title',
                                 queryset=Article.objects.all(),
                                 label='Категория',
                                 empty_label='Любой'
                                 )

    title = CharFilter(lookup_expr='contains', )
