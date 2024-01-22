from django.urls import path
from .views import SearchList, ArticleList, ArticleDetailView, create_Article, ArticleUpdate, ArticleDelete

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_id'),
    path('search/', SearchList.as_view(), name='search'),

    path('create/', create_Article, name='create'),
    path('<int:pk>/updata', ArticleUpdate.as_view(), name='updata'),
    path('<int:pk>/delete/', ArticleDelete.as_view(),name = 'delete'),
]
