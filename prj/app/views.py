from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import ArticleForm
from .filters import ArticleFilter
from .models import Article
from django.urls import reverse_lazy


class ArticleList(ListView):
    model = Article
    template_name = 'app/index.html'
    context_object_name = 'article'
    paginate_by = 10


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'app/article_id.html'
    context_object_name = 'article'


class SearchList(ListView):
    model = Article
    ordering = 'title'
    template_name = 'app/search.html'
    context_object_name = 'article'
    paginate_by = 10

    def get_queryset(self):
        return ArticleFilter(self.request.GET, queryset=super().get_queryset()).qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs), 'filter': self.get_queryset(), }


class ArticleCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Article
    form_class = ArticleForm
    template_name = 'app/create.html'


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app/create.html'
    success_url = reverse_lazy('index')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'app/delete.html'
    success_url = reverse_lazy('index')





@permission_required('polls.add_choice')
@login_required
def my_view (request):
    return LoginRequiredMixin()



#class MyView(LoginRequiredMixin, View):
#    login_url = '/login/'

