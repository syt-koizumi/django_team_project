from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, View
from .models import Mail,ReadMail
from django.urls import reverse_lazy
# from .forms import CheckMailForm

class Mail_list(View):
    def get(self, request):
        mails = Mail.objects.all().order_by('-dtcreated')

        return render(request, 'mail/mail_box.html', {
            'mails': mails
        })


class Mail_detail(DetailView):
    model = Mail
    template_name = 'mail/detail_mail.html'
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        mail = self.get_object()
        read_mail, created = ReadMail.objects.get_or_create(read_mail=mail,user=request.user)
        if not created:
            read_mail.read_count += 1
            read_mail.save()
        # ReadMail.objects.create(read_mail=self.get_object(), user=request.user)
        return response