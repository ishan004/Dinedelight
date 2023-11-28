from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import User_profile , Post


 
@login_required(login_url='login')
def dashboard(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = User_profile.objects.get(user= user_object)
    return render(request, 'social_book/dashboard.html', {'user_profile': user_profile})



@login_required(login_url='login')
def setting(request):
    user_profile = User_profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profile_image
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profile_image = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profile_image = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        return redirect('settings')   
        
    return render(request, 'social_book/setting.html', {'user_profile': user_profile})


@login_required(login_url='login')
def upload_view(request):

    if request.method == 'POST':
        
        user = request.user
        image = request.FILES.get('image_upload')
        print(request.FILES)
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('dashboard')
    else:
        return redirect('dashboard')