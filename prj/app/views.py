from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import ArticleForm
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


class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app/create.html'


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app/create.html'
    success_url = reverse_lazy('index')


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'app/delete.html'
    success_url = reverse_lazy('index')


def create_Article(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ArticleForm()
    data = {'form': form, 'error': error}
    return render(request, 'app/create.html', data)

@permission_required('polls.add_choice')
@login_required
def my_view (request):
    return PermissionRequiredMixin()



#class MyView(LoginRequiredMixin, View):
#    login_url = '/login/'

