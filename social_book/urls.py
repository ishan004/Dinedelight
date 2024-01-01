from django.urls import path
from social_book.views import dashboard, setting, upload_view, post_action_view, profile_view, follow_view, search_view

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', setting, name="settings"),
    path('upload', upload_view, name="upload"),
    path('post_action',post_action_view, name="post_action"),
    path('profile/<uid>/', profile_view, name='profile'),
    path('follow', follow_view, name='follow'),
    path('search/', search_view, name='search'),
    
]
