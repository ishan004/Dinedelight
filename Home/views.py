from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, "Home/index.html")

# views.py
from django.shortcuts import render
from .forms import ContactForm

def contact_section(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you can save to a database, send emails, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For demonstration purposes, we'll just print the data
            print(f"Name: {name}, Email: {email}, Message: {message}")

            # Redirect to a thank you page or any other page after processing
            return HttpResponseRedirect('/thank-you/')  # Adjust the URL as needed
    else:
        form = ContactForm()

    return render(request, 'contact_section.html', {'form': form})

