from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),
    path('lotto_in/', views.lotto_in, name='lotto_in'),
    path('lotto_out/', views.lotto_out, name='lotto_out'),
    path('hello/<str:name>/', views.hello, name='hello'),
    #  Variable Routing => url을 변수화!
]

# Refactoring