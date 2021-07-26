from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.

def send_message(request):
    info = Info.objects.first()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        message="Your Email has been sent! Thanks for reaching us. We will get back to you asap."
        messages.add_message(request, messages.INFO, message)

    context = {'info':info}
    return render(request, 'contact/contact.html', context)