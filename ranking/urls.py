from django.contrib import admin
from django.urls import path,include
from .views import MovieRankingView
from . import views

app_name = 'ranking'
urlpatterns = [
    
    path('', MovieRankingView.as_view(),name = "ranking"),
    # path('', .as_view(), name=''),
    

]