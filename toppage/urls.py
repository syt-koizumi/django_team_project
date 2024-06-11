from django.contrib import admin
from django.urls import path,include
from .views import TopPageView
app_name = "toppage"
urlpatterns = [
    path('', TopPageView.as_view(),name = "toppage"),
    
]