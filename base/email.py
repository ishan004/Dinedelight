from django.conf import settings
from django.core.mail import send_mail
import re

def send_activation_email(email, email_token):
    subject = "Your account needs to be Verified"
    email_from = settings.DEFAULT_FROM_EMAIL
    message = f"Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}"
    send_mail(subject, message, email_from, [email])
        
def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None