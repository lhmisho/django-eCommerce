import math
from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import m2m_changed, pre_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):

    # creating cart object on model so that we can use it where ever we neeed
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)

    # if the id is exits than go else create one
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            # if there is some issue than it's might me ( cart_obj = self.new_cart(user=request.user) )
            cart_obj = Cart.objects.new_cart(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id

        return cart_obj, new_obj
    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    total       = models.DecimalField(default=0.0, decimal_places=2, max_digits=100)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

"""
using m2m signal we are managing calcultion of cart.
"""


# creating signal so that we can calculate our products at the time of shopping
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    products = instance.products.all()
    total = 0
    for x in products:
        total += x.price
    if instance.subtotal != total:
        instance.subtotal = total
        instance.save()
m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

# calculating subtotal like delevary cost etc .....
def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = math.fsum([instance.subtotal,1.8])

pre_save.connect(pre_save_cart_receiver, sender=Cart)












