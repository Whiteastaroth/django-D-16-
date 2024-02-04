from django.forms import ModelForm, TextInput, Textarea
from .models import Article


class ArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = ['title', 'text',  'category', 'author']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название публикации'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст публикации'}),
            'category__title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Категория'}),
        }