from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db.models.signals import pre_save, post_save


from .singnals import object_viewd_singnal
from .utils import get_client_ip

from accounts.signals import user_logged_in

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


def object_viewd_receiver(sender, instance, request, *args, **kwargs):
    # instance.__class__
    content_type = ContentType.objects.get_for_model(sender)

    new_object_view = ObjectViewd.objects.create(
        user        = request.user,
        object_id=instance.id,
        content_type = content_type,
        ip_address=get_client_ip(request),
    )

"I send the sender along with this signal so i don't need to write the sender on connect function"

object_viewd_singnal.connect(object_viewd_receiver)



class UserSession(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # User instance instance id
    ip_address  = models.CharField(max_length=120, blank=True, null=True)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active    = models.BooleanField(default=True)
    ended     = models.BooleanField(default=False)

    def end_session(self):
        session_key = self.session_key
        ended = self.ended
        try:
            Session.objects.get(pk=session_key).delete()
            self.ended = True
            self.active = False
            self.save()
        except:
            pass
        return self.ended

    def __str__(self):
        return self.user.email


def post_save_session_reveiver(sender, instance, created, *args, **kwargs):
    if created:
        qs = UserSession.objects.filter(user=instance.user).exclude(id=instance.id)
        qss = UserSession.objects.filter(user=instance.user).exclude(id=instance.id).count()
        "here the login is if the user logged in more than 3 browser only the last browser will active rest of them deactivated"
        for i in qs:
            if qss >= 2:
                i.end_session()


post_save.connect(post_save_session_reveiver, sender=UserSession)

# def post_save_user_changed_reveiver(sender, instance, created, *args, **kwargs):
#     if created:
#         qs = UserSession.objects.fiuserlter(user=instance.user).exclude(id=instance.id)
#         for i in qs:
#             i.end_session()
#
# post_save.connect(post_save_user_changed_reveiver, sender=User)

def user_logged_in_receiver(sender, instance, request, *args, **kwargs):
    user = instance
    session_key = request.session.session_key
    ip_address  = get_client_ip(request)

    UserSession.objects.create(
        user = user,
        ip_address = ip_address,
        session_key = session_key
    )

user_logged_in.connect(user_logged_in_receiver)


