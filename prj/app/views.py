from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm
from .models import Article
from django.urls import reverse_lazy


class ArticleList(ListView):
    model = Article
    template_name = 'app/index.html'
    ordering = ['-date']
    ontext_object_name = 'article'
    paginate_by = 10


class SearchList(ListView):
    model = Article
    ordering = ['-date']
    template_name = ' search.html'
    context_object_name = 'article'
    paginate_by = 10


class ArticleCreate(PermissionRequiredMixin,  CreateView):
    permission_required = ('news.add_new',)
    model = Article
    form_class = ArticleForm
    template_name = 'new/create.html'


class NewUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_record',)
    model = Article
    form_class = ArticleForm
    template_name = 'new/create.html'
    success_url = reverse_lazy('index')

class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_record',)
    model = Article
    template_name = 'new/news_delete.html'
    success_url = reverse_lazy('index')


@permission_required('polls.add_choice')
@login_required
def my_view (request):
    return PermissionRequiredMixin()



#class MyView(LoginRequiredMixin, View):
#    login_url = '/login/'

