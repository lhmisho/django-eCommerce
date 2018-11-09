from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# import LoginForm, RegisterForm, ContactForm
from .forms import ContactForm

def home_page(request):
    print(request.session.get("firstName", "Unknown")) # get the session property .. like first name
    title = "I am from Home Page"
    content = "Welcome to the home page"
    context = {
        "title"     : title,
        "content"   : content,
    }
    if request.user.is_authenticated:
        context['premium_content'] = "yeeeeee"
    return render(request, 'home.html', context)

def about_page(request):
    title = "I am from About Page"
    content = "Welcome to the about page"
    context = {
        "title"     : title,
        "content"   : content
    }
    return render(request, 'home.html', context)

def contact_page(request):
    title   = "I am from Contact Page"
    content = "Welcome to the contact page"

    # created a instance of ContactForm()
    contact_form = ContactForm(request.POST or None)   # if data is POST request else None
    context = {
        "title"     : title,
        "content"   : content,
        "form"      : contact_form              # passing the form instance to context so that we can access it in view.html as {{form}}
    }

    return render(request, 'contact/view.html', context)
