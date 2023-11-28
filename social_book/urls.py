from django.urls import path
from social_book.views import dashboard, setting, upload_view

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', setting, name="settings"),
    path('upload', upload_view, name="upload"),
]
