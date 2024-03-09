from django.urls import path
from .views import SearchList, ArticleList, ArticleDetailView, ArticleCreate, ArticleUpdate, ArticleDelete, CommentCreate, CommentUpdate, CommentDelete

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_id'),
    path('search/', SearchList.as_view(), name='search'),

    path('create/', ArticleCreate.as_view(), name='create'),
    path('<int:pk>/updata', ArticleUpdate.as_view(), name='updata'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='delete'),
    path('<int:pk>/comment/create/', CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/comment/update/', CommentUpdate.as_view(), name='comment_edit'),
    path('<int:pk>/comment/delete/', CommentDelete.as_view(), name='comment_delete')
]
