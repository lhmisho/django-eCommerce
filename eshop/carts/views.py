from django.shortcuts import render
from .models import Cart

# Create your views here.

# method for create a cart for user.
def crete_cart(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New cart created")
    return cart_obj

def cart_home(request):
    cart_id = Cart.objects.new_or_get(request)
    return render(request, 'carts/cart_home.html', {})