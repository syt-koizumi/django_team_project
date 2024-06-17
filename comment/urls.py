from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import CommentView
app_name = "comment"
urlpatterns = [
      path("",CommentView.as_view(), name="comment"),
]
