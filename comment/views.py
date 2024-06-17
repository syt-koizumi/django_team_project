from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models import Count
from .models import Comment

class CommentView(ListView):
    model = Comment
    template_name = 'comment/comment.html'
    context_object_name = 'comments'

    def get_queryset(self):
        UserComments = Comment.objects.all().order_by('-date')

        return UserComments
