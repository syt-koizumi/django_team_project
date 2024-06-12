
from django.contrib import admin
from django.urls import path,include
from .views import MovieSearchView,MovieDetailView,AddMyList
from django.contrib.auth.decorators import login_required
app_name = "movie"
urlpatterns = [
      path('search', MovieSearchView.as_view(),name = "movie_search"),
      path('search/result/<str:movie_name>', MovieDetailView.as_view(),name = "movie_detail"), 
      path("search/add/<str:name>",login_required(AddMyList),name = "add_mylist"), #mylistに追加するときはログイン必須  
]
