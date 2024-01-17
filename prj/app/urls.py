from django.urls import path
from .views import SearchList, ArticleList, ArticleDetailView

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('search/', SearchList.as_view(), name='search'),
]
