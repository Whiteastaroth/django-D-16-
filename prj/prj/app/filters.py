from django_filters import FilterSet, CharFilter, ChoiceFilter
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
    category = ChoiceFilter(field_name='category',
                            choices=Article.TYPE,
                            label='Категория',
                            empty_label='Любой'
                            )

    title = CharFilter(lookup_expr='contains', )
