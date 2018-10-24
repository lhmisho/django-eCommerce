from django.shortcuts import render
from .models import Cart

# Create your views here.

# method for create a cart for user.
def crete_cart(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New cart created")
    return cart_obj

def cart_home(request):
    request.session['cart_id'] = "12"
    cart_id = request.session.get("cart_id", None)

    if cart_id is None:
        cart_obj = crete_cart()                     # creating cart object for user
        request.session['cart_id'] = cart_obj.id    # geting the id of cart_obj

    else:
        qs = Cart.objects.filter(id=cart_id)

        # if the id is exits than go else create one
        if qs.count() == 1:
            print("Cart id exists")
            cart_obj = qs.first()
        else:
            cart_obj = crete_cart()
            print("New Cart created")
            request.session['cart_id'] = cart_obj.id

    return render(request, 'carts/cart_home.html', {})