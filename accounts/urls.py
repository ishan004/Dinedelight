from django.urls import path
from accounts.views import login_page, register_page, activate_email , logout_view 

urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('activate/<email_token>', activate_email, name="activate"),
    path('logout/', logout_view, name="logout"),
    
    
   
]