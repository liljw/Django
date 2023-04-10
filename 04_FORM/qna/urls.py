from django.urls import path
from . import views

# 똑같은 이름의 url 이 있을 때는 어떡하지? -> 그럴 때를 대신해서 app name과 같이 패턴을 써준다! 
# qna:detail
app_name = 'qna'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/update', views.update, name='update'),
    path('<int:question_pk>/delete', views.delete, name='delete'),
]
