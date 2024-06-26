from django.contrib import admin
from django.urls import path,include
from .views import TopPageView,OpeningView
app_name = "toppage"
urlpatterns = [
    path('', OpeningView.as_view(),name = "opening"),
    path('toppage', TopPageView.as_view(),name = "toppage"),
    
]