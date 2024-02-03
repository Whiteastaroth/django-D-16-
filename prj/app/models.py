from django.db import models
from django.contrib.auth.models import User
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/app/{self.id}'


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


