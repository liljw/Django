from django.urls import path
from . import views

urlpatterns = [
    path('get_lotto/', views.get_lotto),
    path('this_week/', views.this_week),
    path('check_lotto/', views.check_lotto),
    ]