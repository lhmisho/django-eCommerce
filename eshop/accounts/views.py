from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.contrib import messages

# import LoginForm, RegisterForm, ContactForm
from .forms import RegisterForm, LoginForm

# Create your views here.


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
            'form' : form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        #print(form.cleaned_data)
        # geting form data from the form
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            messages.error(request, "Invalid login username or password")
            return redirect('accounts:login')



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
    return render(request, 'registration/register.html', context)