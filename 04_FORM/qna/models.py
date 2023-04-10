from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    reward = models.IntegerField()
    content = models.TextField()
