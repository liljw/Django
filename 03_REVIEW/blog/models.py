from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.pk}: {self.title}'
    

class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)






if __name__ == '__main__':
    # Create 생성 - 첫번째 방법
    a1 = Article()
    a1.title = '첫번째 글'
    a1.content = '첫번째 내용입니다.'
    a1.save()

    # Create 생성 - 두번째 방법
    a2 = Article(title='두번째 글', content='두번째 내용입니다.')
    a2.save()

    # Create 생성 - 세번째 방법
    Article.objects.create(title='세번째 글', content='세번째 내용입니다.')

    # Retrieve(Read) 조회 - 전체 조회
    Article.objects.all()

    # Retrieve(Read) 조회 - 단일 조회
    Article.objects.get(pk=1)

    # Retrieve(Read) 조회 - 레코드의 컬럼별 조회
    a1.title
    a1.content

    # Update 수정 - id 제외하고 모두 수정가능, 접근해서 가져오고, 변경한다음 다시 저장한다.
    a3 = Article.objects.get(pk=3)
    a3.content = '수정한 내용입니다'
    a3.save()

    # Delete 삭제 - Update와 마찬가지로 접근해서 가져오고, 삭제한다.
    a3 = Article.objects.get(pk=3)
    a3.delete()





