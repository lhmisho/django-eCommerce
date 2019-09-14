import stripe
import json
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .models import BillingProfile, Card


STRIPE_SEC_KEY = getattr(settings, "STRIPE_SEC_KEY")
stripe.api_key = STRIPE_SEC_KEY
STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY")


def pyment_method_view(request):
    next_url = None
    # if request.user.is_authenticated:
    #     billingprofile = request.user.billingprofile
    #     my_customer_id = billingprofile.customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")

    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment_method.html', {'publish_key': STRIPE_PUB_KEY, "next_url": next_url})


def payment_method_creat_view(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            raise HttpResponse({"message": "cannot find this user"}, status_code=401)

        print(request.POST)
        token = request.POST.get('token')
        if token is not None:
            new_card_obj = Card.objects.add_new(billing_profile=billing_profile, token=token)

        if new_card_obj:
            print(new_card_obj) # saving our card too!
            print(type(new_card_obj))
        # stripe.Customer.retrieve(billing_profile.customer_id)
        return JsonResponse({"message": "done"})
    raise HttpResponse("error", status_code=401)
