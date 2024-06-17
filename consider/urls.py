
from django.contrib import admin
from django.urls import path,include
from .views import ConsiderStartView,ConsiderResultView,ConsiderTopView
app_name = "consider"
urlpatterns = [
    path("top/",ConsiderTopView.as_view(),name = "top"),
    path("start/",ConsiderStartView.as_view(),name = "start"),
    path("result/",ConsiderResultView.as_view(),name="result"),
   
]
