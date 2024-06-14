from django.contrib import admin
from django.urls import path,include
from .views import UserSearchView,UserMoviesView
from django.urls import path
from . import views

app_name = 'usersearch'
urlpatterns = [
    
    path('search/', UserSearchView.as_view(),name = "user_search"),
    path("user/<int:pk>/movies/",UserMoviesView.as_view(),name ="other_user_movie")

]