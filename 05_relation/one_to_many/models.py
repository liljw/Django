from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 아래와는 반대로, 유저가 없어지면, 해당 유저가 작성한 모든 아티클도 지워진다!

class Comment(models.Model):
    content = models.CharField(max_length=200)
    # Article 모델의 PK를 저장, Article 레코드 삭제시, 관련된 모든 Comment 레코드 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # FK의 경우, 클래스 변수명 뒤에 _id가 자동으로 붙어서 테이블 컬럼이 됨.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


'''
article = Article.objects.create(title='월요일', content='싫어요')
a1 = article

c1 = Comment.objects.create(content='맞아맞아', article_id=1)
c2 = Comment.objects.create(content='짱싫다', article_id=a1.id)
c3 = Comment.objects.create(content='난 좋음', article=a1)

# c1 댓글이 달린 게시글
c1.article
# c1 댓글이 달린 게시글의 목록
c1.article.title

# a1에 달린 모든 댓글
a1.comment_set.all()
a1 = Article.objects.filter(pk=article_id)
# a1에 달린 댓글들을 pk 역정렬
a1.comment_set.order_by('-pk')

'''