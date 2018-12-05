from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


User = settings.AUTH_USER_MODEL
# Create your models here.

class ObjectViewd(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) # User instance instance id
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE) # User, Product, Order, Cart etc
    object_id       = models.PositiveIntegerField() # User id, Product id, Order id etc
    content_object  = GenericForeignKey('content_type','object_id') # Pordut instance
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return "%s viewed on %s" %(self.content_object, self.timestamp)
        return (f'{self.content_object} viewed on {self.timestamp}')

    class Meta:
        "Most recent save show up first"
        ordering = ['-timestamp']
        verbose_name = 'Object viewd'
        verbose_name_plural = 'Objects viewd'
