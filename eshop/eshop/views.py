from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


# import ContactForm from .form
from .forms import ContactForm

# import LoginForm
from .forms import LoginForm

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

    # created a instance of ContactForm()
    contact_form = ContactForm(request.POST or None)   # if data is POST request else None
    context = {
        "title"     : title,
        "content"   : content,
        "form"      : contact_form              # passing the form instance to context so that we can access it in view.html as {{form}}
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # checking is this request is POST or not
    # if request.method == "POST":
    #     print(request.POST)          # printing the requested value as dict
    #     print(request.POST.get('fullname'))   # printing the acutal requested value
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, 'contact/view.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
            'form' : form
    }
    #print(request.user.is_authenticated)
    if form.is_valid():
        print("User is not loged in")
        #print(form.cleaned_data)
        # geting form data from the form
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            #context['form'] = LoginForm()
            return redirect('/login')
        else:
            print("Error")
    
    
    
    return render(request, 'registration/login.html', context)

def register_page(request):
    return render(request, 'register.html')