from django_filters import FilterSet, CharFilter, ChoiceFilter, AuthorFilter
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

    author = AuthorFilter(field_name='author', lookup_expr='gt', label='Автор', widget=AuthorFilter(attrs={'type': 'author'}, ))
