from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique=True)
    #full_name = models.CharField(max_length=255, blank=True, null=True)
    active  = models.BooleanField(default=True)     # can login
    staff   = models.BooleanField(default=False)    # staff user non super user
    admin   = models.BooleanField(default=False)    # superuser
    timestamp  = models.DateTimeField(auto_now_add=True)
    #confirm = models.BooleanField(default=False)
    #confirmed_at = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email'  #username

    # USERNAME_FIELD AND  password are required default
    REQUIRED_FIELDS = []

    def __str__(self):
        # __unicode__ return
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

class GuestEmail(models.Model):
    email   = models.EmailField()
    active  = models.BooleanField(default=True)
    updateat    = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email