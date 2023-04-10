# Generated by Django 3.2.18 on 2023-04-09 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_like_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stars',
            field=models.ManyToManyField(related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
    ]
