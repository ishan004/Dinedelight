from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_profile, Post
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import re
from django import forms
from django.core.exceptions import ValidationError




def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username= email)
        
        if not user_obj.exists():
            messages.warning(request, "Account does not exist")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Account is not verified")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/social_book/dashboard')
        
        messages.warning(request, "Invalid username or password")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')



class RegistrationForm(forms.Form):
    
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Additional email validation using a regular expression
            
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{2,29}$', username):
                form.add_error('first_name', 'Invalid format')
                
            if not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
                form.add_error('email', 'Invalid email format')

                return render(request, 'accounts/register.html', {'form': form})

            user_obj = User.objects.filter(username=email)
            if user_obj.exists():
                messages.warning(request, "Email already registered")
                return HttpResponseRedirect(request.path_info)

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, "An email has been sent to your mail.")
            return HttpResponseRedirect(request.path_info)
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})




def activate_email(request,email_token):
    try:
        user= User_profile.objects.get(email_token = email_token)
        user.is_email_verified= True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse("Invalid email token")
    
