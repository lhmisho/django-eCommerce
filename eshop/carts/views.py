from django.shortcuts import render
from .models import Cart

# Create your views here.

# method for create a cart for user.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/cart_home.html', {})