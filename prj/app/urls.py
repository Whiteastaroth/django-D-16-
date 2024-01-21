from django.urls import path
from .views import SearchList, ArticleList, ArticleDetailView, ArticleCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('search/', SearchList.as_view(), name='search'),

    path('create/', ArticleCreate.as_view(), name='create'),
]
