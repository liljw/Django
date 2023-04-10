from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Article

class User(AbstractUser):
    like_articles = models.ManyToManyField(Article, related_name='like_users')
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')
    


