from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Article (models.Model):
    TYPE = (
        ('tank', 'Танк'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('guildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')

    def preview(self):
        preview = f'{self.text[:128]}...'
        return preview

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/app/{self.id}'


class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} : {self.text} [:20] + ...'

    def get_absolute_url(self):
        return reverse( 'article_id', kwargs={'pk': self.article_id})
