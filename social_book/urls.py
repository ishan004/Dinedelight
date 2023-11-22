from django.urls import path
from social_book.views import dashboard

urlpatterns = [
    path('profile/', dashboard, name='dashboard')
]
