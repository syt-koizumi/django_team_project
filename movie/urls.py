
from django.contrib import admin
from django.urls import path,include
from .views import MovieSearchView,MovieSearchResultView
app_name = "movie"
urlpatterns = [
      path('/search', MovieSearchView.as_view(),name = "movie_search"),
      path('/search/result/<str:movie_name>/<str:resultdata>',  MovieSearchResultView.as_view(),name = "search_result"),
      
]
