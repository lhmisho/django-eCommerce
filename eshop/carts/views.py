from django.shortcuts import render, redirect
from .models import Cart

from products.models import Product
# Create your views here.

# method for create a cart for user.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/cart_home.html', {})

# Update view for cart
def cart_update(request):
    product_id  = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)    # we also added this line to products view on get_context_data so that we can add cart to specific product

    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")