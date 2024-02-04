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
        queryset = super().get_queryset()
        self.filter = ArticleFilter(self.request.GET, queryset)
        return self.filter.qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['filter'] = self.filter
        return context


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

#def usual_login_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    is user is not None:
#    OneTimeCode.objects.create(code=randome.choice('abcde'), user=user)
#    else:


#def login_with_code_view(request):
#    username = request.POST['username']
#    code = request.POST['code']


#class MyView(LoginRequiredMixin, View):
#    login_url = '/login/'

