
from django.contrib import admin
from django.urls import path,include

app_name = "movie"
urlpatterns = [
      path('', TopPageView.as_view(),name = "toppage"),
]
