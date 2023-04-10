# myapp/urls.py

from django.urls import path
from . import views
# 현재 파일 위치와 같은 위치에 views.py를 import

urlpatterns = [
    path('hello/', views.hello),

    path('bye/', views.bye),

    path('review/', views.review),

    path('index/', views.index),
]