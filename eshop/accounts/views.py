from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import is_safe_url

from .forms import *
from .models import *
# Create your views here.

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
            'form' : form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id

        if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")



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
            try:
                del request.session['guest_email_id']
            except:
                pass
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
        form.save()
    return render(request, 'registration/register.html', context)
