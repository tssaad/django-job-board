from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile

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
            return redirect(reverse('accounts:profile'))
        else:
            message="Somthing Worng happened. Please check your data."
            messages.add_message(request, messages.INFO, message)
    else:
        form=SignupForm()
    context = {'form' : form}
    return render(request, 'registration/signup.html', context)

def profile(request):
    profile = Profile.objects.get(PRFUser=request.user)
    context = {'profile' : profile}
    return render(request, 'accounts/profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(PRFUser=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofileform = profileform.save(commit=False)
            myprofileform.PRFUser = request.user
            message = "Your Profile has been updated sucessfully!"
            messages.add_message(request, messages.INFO, message)            
            return redirect(reverse("accounts:profile"))
        else:
            message="Somthing Worng happened. Please check your data."
            messages.add_message(request, messages.INFO, message)                        
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {'userform':userform, 'profileform':profileform} 
    return render(request, 'accounts/profile_edit.html', context)   