from django.urls import path    
from Home.views import index, contact_section

urlpatterns = [
    path('', index, name='index'),
    path('contact-section/', contact_section, name='contact_section'),
]
