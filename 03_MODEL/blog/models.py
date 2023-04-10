from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # TimeStamp add는 생성될 때만! now는 수정될 때 마다!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # <Article #1 : 안녕하세요>
        return f'#{self.pk}: {self.title}'
    
