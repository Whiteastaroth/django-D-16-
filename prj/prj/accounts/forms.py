from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import mail_managers, mail_admins
from django.core.mail import EmailMultiAlternatives

from allauth.account.forms import SignupForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        subject = 'Добро пожаловать в наш интернет-магазин!'
        text = f'{user.username}, Вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, Вы успешно зарегистрировались на сайте '
            f'<a href="http://127.0.0.1:8000/"> NEW autoBASS</a>!'
        )

        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )

        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
