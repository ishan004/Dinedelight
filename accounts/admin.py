from django.contrib import admin
from .models import User_profile, Post, LikePost, Followers

# Register your models here.
admin.site.register(User_profile)

admin.site.register(Post)

admin.site.register(LikePost)
admin.site.register(Followers)
