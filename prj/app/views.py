from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


from .forms import ArticleForm, UserResponseForm
from .filters import ArticleFilter
from .models import Article, UserResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect


class ArticleList(ListView):
    model = Article
    template_name = 'app/index.html'
    context_object_name = 'article'
    paginate_by = 10


class CommentCreate(LoginRequiredMixin, CreateView):
    model = UserResponse
    template_name = 'app/article_id.html'
    form_class = UserResponseForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.article_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)


class CommentUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = UserResponse
    template_name = 'app/comment_edit.html'
    form_class = UserResponseForm
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.email.endswith("@example.com")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_author'] = UserResponse.objects.get(pk=self.kwargs.get('pk')).author
        return context


class CommentDelete(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = UserResponse
    template_name = 'app/comment_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.email.endswith("@example.com")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_author'] = UserResponse.objects.get(pk=self.kwargs.get('pk')).author
        return context


class ArticleDetailView(DetailView, CommentCreate):
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

    def form_valid(self, form):
        article = form.save(commit= False)
        article.author = self.request.user
        article.save()
        return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Article
    form_class = ArticleForm
    template_name = 'app/edit.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.email.endswith("@example.com")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_author'] = Article.objects.get(pk=self.kwargs.get('pk')).author
        return context


class ArticleDelete(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Article
    template_name = 'app/delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.email.endswith("@example.com")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_author'] = Article.objects.get(pk=self.kwargs.get('pk')).author
        return context





@permission_required('polls.add_choice')
@login_required
def my_view (request):
    return LoginRequiredMixin()




#class MyView(LoginRequiredMixin, View):
#    login_url = '/login/'

