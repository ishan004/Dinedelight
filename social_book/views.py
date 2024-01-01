from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import User_profile , Post, LikePost, Followers
# from django.shortcuts import get_object_or_404
from itertools import chain


 
@login_required(login_url='login')
def dashboard(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = User_profile.objects.get(user=user_object)
    
    
    user_following_list = []
    feed = []

    user_following = Followers.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user__username=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))
    
    
    
    # posts = Post.objects.all()
    context = {
        'user_profile': user_profile,
        'posts': feed_list,
        # 'posts': posts,
    }
    return render(request, 'social_book/dashboard.html', context=context) 



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

@login_required(login_url='login')
def post_action_view(request):
    user = request.user
    post_id = request.GET.get('post_id')
    
    post = Post.objects.get(uid=post_id)
    
    like_filter = LikePost.objects.filter(post_id=post_id, user=user).first()
    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, user=user)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('dashboard')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('dashboard')
    

@login_required(login_url='login')
def profile_view(request, uid):
   
    
    user_object = User.objects.get(username=uid)
    user_profile = User_profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=user_object)
    user_post_length = len(user_posts)
    
    follower = request.user.username
    user = user_object
    
    if Followers.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
    
    
    user_followers = len(Followers.objects.filter(user=user_object))
    user_following = len(Followers.objects.filter(follower=user_object))
    
    context= {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,   
        'user_followers' : user_followers,
        'user_following' : user_following,
    }
    
    return render(request, 'social_book/profile.html', context=context)


@login_required(login_url='login')
def follow_view(request):
    if request.method == 'POST':
        follower = request.POST.get('follower')
        user = request.POST.get('user')
        
        if Followers.objects.filter(follower=follower, user=user).first():
            delete_follower= Followers.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/social_book/profile/'+user)
        else:
            new_follower = Followers.objects.create(follower=follower,user=user)
            new_follower.save()
            return redirect('/social_book/profile/'+user)
    else:
        return redirect('dashboard')
    
@login_required(login_url='login')
def search_view(request):
    
    user_object = User.objects.get(username=request.user.username)
    user_profile = User_profile.objects.get(user=user_object)
    
    if request.method=='POST':
        username=request.POST['username']
        
        username_object = User.objects.filter(username__icontains=username)
        
        username_profile = []
        username_profile_list = []
        
        for users in username_object:
            username_profile.append(users.id)
        
        
        for ids in username_profile:
            profile_lists = User_profile.objects.filter(user_id=ids)
            
            username_profile_list.append(profile_lists)
          
        username_profile_list  = list(chain(*username_profile_list))
        print(username_profile_list)
    return render(request, 'social_book/search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})

