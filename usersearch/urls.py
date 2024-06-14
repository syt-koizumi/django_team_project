from django.contrib import admin
from django.urls import path,include
from .views import UserSearchView,UserSearchResultView
from django.urls import path
from . import views

app_name = 'usersearch'
urlpatterns = [
    
    path('', UserSearchView.as_view(),name = "usersearch"),
    path("search/",UserSearchResultView.as_view(),name ="usersearchresult")

]