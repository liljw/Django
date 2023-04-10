from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # new - user에게 글을 작성할 수 있는 form이 적혀있는 html을 제공.
    # path('new/', views.new, name='new'),
    
    # create - new에서 user가 작성한 form의 데이터를 POST로 받아서 저장.
    path('create/', views.create, name='create'),

    # index - 전체 게시글 (Article 전체)를 조회할 수 있는 html을 제공.
    path('', views.index, name='index'),

    # detail - 특정 게시글을 조회할 수 있는 html을 제공.
    path('<int:article_pk>/', views.detail, name='detail'),

    # edit - 특정 게시글을 수정할 수 있는 html을 제공.
    # path('<int:article_pk>/edit/', views.edit, name='edit'),

    # update - edit에서 user가 수정한 form의 데이터를 POST로 받아서 저장.
    path('<int:article_pk>/update/', views.update, name='update'),

    # delete - 특정 게시글을 삭제.
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    # blog/1/replies/create - 특정 게시글에 댓글을 생성
    path('<int:article_pk>/replies/create/', views.create_reply, name='create_reply'),

    # blog/1/replies/1/create - 특정 게시글의 특정 댓글을 삭제
    path('<int:article_pk>/replies/<int:reply_pk>/delete/', views.delete_reply, name='delete_reply'),

    # 1/like_article - 특정 게시글에 좋아요
    path('<int:article_pk>/like_article', views.like_article, name='like_article'),
    

]
