from django.urls import path
from .views import create_mail

app_name = 'mail'
urlpatterns = [
    path('',create_mail.as_view(), name='mail_list'),
]
