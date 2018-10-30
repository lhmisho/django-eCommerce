from django.db import models
from django.db.models.signals import pre_save
from eshop.utils import unique_order_id_generator
from carts.models import Cart
# Create your models here.

ORDER_STATUS_CHOICE = (
    ('created', 'CREATED'),
    ('paid', 'PAID'),
    ('shipped', 'SHIPPING'),
    ('refounded', 'REFOUNDED')
)

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    #billing_profile     =
    #shipping_address    =
    #billing_address     =
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status  = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICE)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total   = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)


    def __str__(self):
        return self.order_id

# using pre_save singnals with unique_order_generator for saving the unique order id
def pre_save_order_id(sender, instance, *args, **kewarg):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_order_id , sender=Order)