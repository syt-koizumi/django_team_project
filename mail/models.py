from django.db import models
from accounts.models import CustomUser

class Mail(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=100)
    dtcreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ReadMail(models.Model):
    read_mail = models.ForeignKey(Mail, verbose_name="メール", related_name='read_mail', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザ名", related_name='user', on_delete=models.CASCADE)
    read_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.read_mail)
