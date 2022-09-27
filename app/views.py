from email import message
from django.shortcuts import render
from .models import Projects
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    project = Projects.objects.all()

    messageSent = False

    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            message = cd['message']

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            messageSent = True
    else:
        form = EmailForm()

    context = {
        'project':project,
        'form':form,
        'messageSent':messageSent,
    }
    return render(request, 'app/index.html', context)

