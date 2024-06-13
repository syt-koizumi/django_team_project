
from django.contrib import admin
from django.urls import path,include
from .views import MylistView,DeleteView
from django.urls import path
from . import views

app_name = 'mypage'
urlpatterns = [
    
    path('mylist/', MylistView.as_view(),name = "mylist"),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    

]