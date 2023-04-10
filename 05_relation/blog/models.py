from django.db import models
from django.conf import settings

class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    # Posting 모델의 PK를 저장, Posting 레코드 삭제시, 관련된 모든 Comment 레코드 삭제
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    # FK의 경우, 클래스 변수명 뒤에 _id가 자동으로 붙어서 테이블 컬럼이 됨.