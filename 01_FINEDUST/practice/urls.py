from django.urls import path
from . import views

urlpatterns = [
    path('get_info/', views.get_info),
]
