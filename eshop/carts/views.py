from django.shortcuts import render
from .models import Cart

# Create your views here.

# method for create a cart for user.
def crete_cart(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New cart created")
    return cart_obj

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)

    # if the id is exits than go else create one
    if qs.count() == 1:
        cart_obj = qs.first()
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new_cart(user=request.user)
        request.session['cart_id'] = cart_obj.id

    return render(request, 'carts/cart_home.html', {})