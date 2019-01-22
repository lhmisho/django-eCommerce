from django.shortcuts import render

import stripe
stripe.api_key = "sk_test_Lv83uXj8SaWmUUhMKxBzratw"

STRIPE_PUB_KEY = "pk_test_UYuzHdmsbb4URaYMjocxJPZP"

def pyment_method_view(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'billing/payment_method.html', {'publish_key': STRIPE_PUB_KEY})