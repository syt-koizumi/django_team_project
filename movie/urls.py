
from django.contrib import admin
from django.urls import path,include
from .views import MovieSearchView,MovieDetailView
app_name = "movie"
urlpatterns = [
      path('search', MovieSearchView.as_view(),name = "movie_search"),
      path('search/result/<str:movie_name>', MovieDetailView.as_view(),name = "movie_detail"), 
]
