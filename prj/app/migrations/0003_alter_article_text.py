# Generated by Django 5.0 on 2024-01-22 15:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
