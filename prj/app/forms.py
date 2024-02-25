from django.forms import ModelForm, TextInput, Textarea
from .models import Article, UserResponse


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'text',  'category']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название публикации'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст публикации'}),
            'category__title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Категория'}),
        }


class UserResponseForm(ModelForm):

    class Meta:
        model = UserResponse
        fields = ['text',]
        labels = {
            'text': 'Комментируйте'
        }

        widgets = {
            'text': Textarea(attrs={'class': 'form-text', 'cols': 200, 'rows': 4}),
        }
