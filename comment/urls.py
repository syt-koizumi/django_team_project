from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import CommentView, like_comment, CommentDeleteView
app_name = "comment"
urlpatterns = [
      path("",CommentView.as_view(), name="comment"),
      path('like/<int:comment_id>/', login_required(like_comment), name='like_comment'),
      path('delete/<int:pk>/', CommentDeleteView.as_view(), name='delete'),
]
