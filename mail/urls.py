from django.urls import path
from .views import Mail_list, Mail_detail

app_name = 'mail'
urlpatterns = [
    path('', Mail_list.as_view(), name='mail_list'),
    path('detail/<int:pk>', Mail_detail.as_view(), name='mail_detail'),
]
