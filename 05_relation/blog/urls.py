from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.create_posting, name="create_posting"),
    path('', views.posting_index, name='posting_index'),
    path('<int:posting_pk>/', views.posting_detail, name='posting_detail'),
    path('<int:posting_pk>/update/', views.update_posting, name='update_posting'),
    path('<int:posting_pk>/delete/', views.delete_posting, name='delete_posting'),

    # blog/1/replies/create/
    path('<int:posting_pk>/replies/create/', views.create_reply, name="create_reply"),
    # blog/1/replies/1/delete/
    path('<int:posting_pk>/replies/<int:reply_pk>/delete/', views.delete_reply, name="delete_reply"),
    
    # blog/1/like_posting/
    path('<int:posting_pk>/like_posting', views.like_posting, name='like_posting'),

    # blog/feed
    path('feed/', views.feed, name='feed'),
    
]
