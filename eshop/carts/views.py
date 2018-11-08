from django.shortcuts import render, redirect
from .models import Cart
from orders.models import Order
from products.models import Product
# Create your views here.

# method for create a cart for user.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        "cart" : cart_obj,
    }
    return render(request, 'carts/cart_home.html', context)

# Update view for cart
def cart_update(request):
    # getting the product_id which is sent from the update_cart.html
    product_id  = request.POST.get('product_id')

    # if the product_id is not none then we taking it to product_obj
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except DoesNotExist:
            return redirect("cart:home")   # if product is not exists simply just redirect to home
        cart_obj, new_obj = Cart.objects.new_or_get(request)    # we also added this line to products view on get_context_data so that we can add cart to specific product

        # if the product_obj is exists in cart than we can remove
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        # if the product_obj is exists in cart than we can add it
        else:
            cart_obj.products.add(product_obj)
        #return redirect(product_obj.get_absolute_url())
        request.session['total_product'] = cart_obj.products.count()
    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    return render(request, 'carts/checkout.html', {'object':order_obj})