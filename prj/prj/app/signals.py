from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from models import UserResponse

from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.conf import settings

from .models import Article


@receiver(post_save, sender=UserResponse)
def my_handler(sender, instance, created, **kwargs):
    mail = instance.article.author.email
    send_mail(
        'Subject here',
        'Here is the message. ',
        'host@mail.ru',
        [mail],
        fail_silently=False,
    )


@receiver(post_save, sender=Article)
def New_created(instance, sender, created, **kwargs):
    print('Создан товар', instance)
    if created:
        emails = User.objects.filter(subscriptions__category=instance.category).values_list('email', flat=True)

        subject = f'Новая запись в категории {instance.category}'

        text_content = (
            f'Название: {instance.title}\n'
            f'Анонс: {instance.preview()}\n\n'
            f'Ссылка на публикацию: {settings.SITE_URL}{instance.get_absolute_url()}'
        )
        html_content = (
            f'Название: {instance.title}<br>'
            f'Анонс: {instance.preview()}<br><br>'
            f'<a href="{settings.SITE_URL}{instance.get_absolute_url()}">'
            f'Ссылка на публикацию</a>'
        )
        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
