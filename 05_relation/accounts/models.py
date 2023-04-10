from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.models import Posting

class User(AbstractUser):
    # mbti = models.CharField(max_length=4, null=True 아니면 default='INTP')
    like_postings = models.ManyToManyField(Posting, related_name='like_users')
    # 'self'는 나 스스로를 참조한다는 말! 원래는 settings를 import해줘서 settings.AUTH_USER_MODEL을 해줘야 하는데, 자기 참조만!
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')


'''
u1.like_postings.add(p1)
p1.like_users.add(u1)

위의 두 개는 똑같음..!
'''