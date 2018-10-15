from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# import LoginForm, RegisterForm, ContactForm
from .forms import RegisterForm, LoginForm, ContactForm

def home_page(request):
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

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
            'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email    = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        # creating new user
        new_user = User.objects.create(username, email, password)
        print(new_user)
    return render(request, 'registration/register.html', context)