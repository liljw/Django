"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Master URLs (intro/urls.py)
from django.contrib import admin
from django.urls import path

#    폴더(패키지)    파일(모듈)
# from myapp import views
# from hair import views

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 접두사가 'myapp/'이면, myapp/urls.py로 던질래
    path('myapp/', include('myapp.urls')),
    # 접두사가 'hair/'면, hair/urls.py로 던질래
    path('hair/', include('hair.urls')),
    # path('hello/', views.hello),  
    # # 127.0.0.0/a 라고 주소창에 매개변수 1을 입력받으면, 매개변수 2를 실행한다. 
    
    path('yourapp/', include('yourapp.urls')),
    
    path('utilities/', include('utilities.urls'))

    # path('bye/', views.bye),
    # # path('이러한 url패턴으로 요청이 들어오면/', 실행할 함수)

    # path('asdf/', ), 
]

