from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_profile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login_page(request):
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

       
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        
        if user_obj.exists():
            messages.warning(request, "Email already registered")
            return HttpResponseRedirect(request.path_info)
        
        print(email)
        
        user_obj = User.objects.create(first_name = first_name, last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()
        
        messages.success(request, "An email has been sent to your mail.")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')


def activate_email(request,email_token):
    try:
        user= User_profile.objects.get(email_token = email_token)
        user.is_email_verified= True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse("Invalid email token")