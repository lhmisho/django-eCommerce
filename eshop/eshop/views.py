from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = "I am from Home Page"
    content = "Welcome to the home page"
    context = {
        "title"     : title,
        "content"   : content
    }
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
    context = {
        "title"     : title,
        "content"   : content
    }

    # checking is this request is POST or not
    if request.method == "POST":
        print(request.POST)          # printing the requested value as dict
        print(request.POST.get('fullname'))   # printing the acutal requested value
        print(request.POST.get('email'))
        print(request.POST.get('content'))

    return render(request, 'contact/view.html', context)
