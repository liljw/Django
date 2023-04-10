from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    rank = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f'#{self.pk}: {self.title}'
