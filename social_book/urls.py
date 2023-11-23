from django.urls import path
from social_book.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard')
]
