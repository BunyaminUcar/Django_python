#http://127.0.0.1:8000/ ==> index.html
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]