#http://127.0.0.1:8000/ ==> index.html
from django.urls import path
from . import views

#http://127.0.0.1:8000/  ==> anasayfa.html
#http://127.0.0.1:8000/index  ==> anasayfa.html
#http://127.0.0.1:8000/login  ==> login.html

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('login', views.login),
    
]
