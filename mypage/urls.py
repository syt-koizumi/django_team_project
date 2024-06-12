
from django.contrib import admin
from django.urls import path,include
from .views import MylistView
from django.urls import path
from . import views

app_name = 'mypage'
urlpatterns = [
    
    path('mylist/', MylistView.as_view(),name = "mylist"),

]