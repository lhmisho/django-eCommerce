from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from accounts.models import GuestEmail
# Create your models here.

import stripe
stripe.api_key = "sk_test_Lv83uXj8SaWmUUhMKxBzratw"

User = settings.AUTH_USER_MODEL

class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        obj = None
        created = False
        if user.is_authenticated:
            'this is loged in user checkout; remind checkout'
            obj, created = self.model.objects.get_or_create(user=user, email=user.email)

        elif guest_email_id is not None:
            'this is guest user checkout; auto payment checkout'
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj, created = self.model.objects.get_or_create(email=guest_email_obj.email)
        else:
            pass
        return obj, created




class BillingProfile(models.Model):
    user    = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    email   = models.EmailField(unique=True)
    active  = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updateat  = models.DateTimeField(auto_now=True)
    customer_id = models.CharField(max_length=120, blank=True, null=True)

    objects = BillingProfileManager()

    def __str__(self):
        return self.email

# for stripe integration
def billing_profile_created_receiver(sender, instance, *args, **kwargs):
    if not instance.customer_id and instance.email:
        print("Stripe Api request")
        customer = stripe.Customer.create(
            email = instance.email
        )
        print(customer)
        instance.customer_id = customer.id

pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)


def user_created_receiver(sender, instance, created,*args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)