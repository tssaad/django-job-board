from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            message = "The profile has been opened sucessfully!"
            messages.add_message(request, messages.INFO, message)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            message = "You have been logined sucessfully!"
            messages.add_message(request, messages.INFO, message)
            return redirect(reverse('jobs:job_list'))
        else:
            message="Somthing Worng happened. Please check your data."
            messages.add_message(request, messages.INFO, message)
    else:
        form=SignupForm()
    context = {'form' : form}
    return render(request, 'registration/signup.html', context)