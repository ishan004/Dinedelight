from django.shortcuts import render
from django.http import HttpResponseRedirect
import csv
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    return render(request, "Home/index.html")

# views.py

from .forms import ContactForm

def contact_section(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you can save to a database, send emails, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            file = open('responses.csv', 'a')
            writer = csv.writer(file)
            writer.writerow([name,email,message])
            file.close()
            
            EmailMessage(
               'Contact Form From {}'.format(name),
               message,
               'form-response@example.com', # Send from (your website)
               ['ishanbhusal0@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

            # For demonstration purposes, we'll just print the data
            print(f"Name: {name}, Email: {email}, Message: {message}")

            # Redirect to a thank you page or any other page after processing
            return render(request, 'Home/index.html')  # Adjust the URL as needed
    else:
        form = ContactForm()

    return render(request, 'contact_section.html', {'form': form})

         
   
  



