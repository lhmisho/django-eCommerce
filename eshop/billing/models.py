from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user    = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    email   = models.EmailField(unique=True)
    active  = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updateat  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


def user_created_receiver(sender, instance, created,*args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)