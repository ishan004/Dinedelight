from django.urls import path    
from Home.views import index

urlpatterns = [
    path('', index, name='index'),
]
