
from django.contrib import admin
from django.urls import path,include
from .views import ConsiderView
app_name = "consider"
urlpatterns = [
    
    path("",ConsiderView.as_view(),name = "consider")
   
]
