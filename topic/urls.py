from django.contrib import admin
from django.urls import path,include
from.views import TopicTop
app_name = "topic"
urlpatterns = [
    path('top', TopicTop.as_view(),name = "top"),
]
