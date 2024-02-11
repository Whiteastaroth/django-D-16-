import random

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from string import hexdigits
from .models import OneTimeCode
from .forms import SignUpForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = SignUpForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
        return redirect('code', request.POST['username'])


class GetCode(CreateView):
    success_url = 'accounts/code'
    template_name = 'registration/code.html'

    def get_context_data(self, **kwargs):
        username = self.kwargs.get('user')
        if not OneTimeCode.objects.filter(user=username).exits():
            code = ''.join(random.sample(hexdigits, 5))
            OneTimeCode.objects.create(user=username, code=code)
            user = User.objects.get(username=username)
            send_mail(
                subject=f'Код активации',
                message=f' Код активации аккаунта:, {code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = request.path.splite('/')[-1]
            if OneTimeCode.objects.filter(code=request.POST['code'], user=user).exits():
                User.objects.filter(username=user).update(is_active=True)
                OneTimeCode.objects.filter(code=request.POST['code'], user=user).delite()
            else:
                return render(self.request, 'accounts/invalid_code.html')
