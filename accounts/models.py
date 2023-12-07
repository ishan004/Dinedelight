from django.db import models
from django.contrib.auth.models import User
from base.models import base_model
from django.db.models.signals import post_save
from django.dispatch import receiver 
import uuid
from base.email import send_activation_email
from datetime import datetime


class User_profile(base_model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True,blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_image= models.ImageField(upload_to ='profile_image/', default="/profile_image/blank-profile-picture.png")
    
    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender = User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created :
            email_token = str(uuid.uuid4()) 
            User_profile.objects.create(user=instance, email_token=email_token)
            email = instance.email
            send_activation_email(email,email_token)
    except Exception as e:
        print(e)



class Post(base_model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to='post_images/')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    no_of_likes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user.username
    
    
    
    
    
    class Meta:
        ordering= ['-created_at']    
    
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likepost")
    
    def __str__(self):
        return self.user.username
    


class Followers(models.Model):
    follower = models.CharField(max_length=100)   
    user = models.CharField(max_length=100)
    

    
    
    def __str__(self):
        return self.user

    
    
    