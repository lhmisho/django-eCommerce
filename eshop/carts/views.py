import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse
from accounts.forms import GuestForm, LoginForm
from accounts.models import GuestEmail
from address.forms import AddressForm
from address.models import Address
from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from .models import Cart

# Create your views here.

# method for create a cart for user.

STRIPE_SEC_KEY = getattr(settings, "STRIPE_SEC_KEY")
stripe.api_key = STRIPE_SEC_KEY
STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY")

def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products    = [
        {
            "title":x.title,
            "price":x.price,
            "url":x.get_absolute_url(),
            "id":x.id,
            "slug":x.slug
        } for x in cart_obj.products.all()]

    # products_list = []
    # for x in cart_obj.products.all():
    #     products_list.append({"title:":x.title, "price":x.price})

    cart_data   = {"products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total}
    return  JsonResponse(cart_data)


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
            data_added = False
        # if the product_obj is exists in cart than we can add it
        else:
            cart_obj.products.add(product_obj)
            data_added = True

        # return redirect(product_obj.get_absolute_url())
        request.session['total_product'] = cart_obj.products.count()

        if request.is_ajax():
            print("Ajax request")
            json_data = {
                'added'     : data_added,
                'removed'   : not data_added,
                'itemCount' : cart_obj.products.count(),
            }
            return  JsonResponse(json_data)
    return redirect("cart:home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)

    if not request.user.is_authenticated:
        billing_profile = None

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    has_card = False
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]

        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]

        if billing_address_id or shipping_address_id:
            order_obj.save()

        has_card = billing_profile.has_card

    if request.method == "POST":
        "check the cart process done"
        is_prepared = order_obj.check_done()
        if is_prepared:
            did_chared, crg_msg = billing_profile.charge(order_obj)
            if did_chared:
                order_obj.mark_paid()
                request.session['total_product'] = 0
                del request.session['cart_id']
                if not billing_profile.user:
                    billing_profile.set_card_inactive()
                return redirect("cart:success")
            else:
                print(crg_msg)
                return redirect("cart:checkout")
    context = {
        'object': order_obj,
        'billing_profile' : billing_profile,
        'login_form' : login_form,
        'guest_form' : guest_form,
        'address_form' : address_form,
        'address_qs' : address_qs,
        "has_card": has_card,
        "publish_key": STRIPE_PUB_KEY
    }
    return render(request, 'carts/checkout.html', context)


def checkout_done(request):
    return render(request, 'carts/checkout-done.html',{})
