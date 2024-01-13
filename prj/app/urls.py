from django.urls import path
from .views import SearchList, ArticleList

urlpatterns = [
    path('', ArticleList.as_view(template_name='index.html'), name='index'),
    path('search/', SearchList.as_view(template_name='search.html'), name='search'),
]
