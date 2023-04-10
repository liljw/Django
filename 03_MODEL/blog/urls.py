# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Create의 영역
    path('new/', views.new, name='new'),
    # 사용자 입력 데이터가 함께 들어옴!
    path('create/', views.create, name='create'),
    # Read/ Retrieve의 영역
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    # Update
    # blog/1/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # blog/1/update
    path('<int:article_pk>/update/', views.update, name='update'),

    # Delete
    # blog/1/delete
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]
