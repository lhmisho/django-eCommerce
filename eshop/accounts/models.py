from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have an password")
        if not full_name:
            raise ValueError("User must have fullname")

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )

        user_obj.set_password(password)
        user_obj.staff  = is_staff
        user_obj.admin  = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

    def create_staffuser(self,full_name, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,full_name, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active  = models.BooleanField(default=True)     # can login
    staff   = models.BooleanField(default=False)    # staff user non super user
    admin   = models.BooleanField(default=False)    # superuser
    timestamp  = models.DateTimeField(auto_now_add=True)
    #confirm = models.BooleanField(default=False)
    #confirmed_at = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email'  #username

    # USERNAME_FIELD AND  password are required default
    REQUIRED_FIELDS = ['full_name']
    objects = UserManager()

    def __str__(self):
        # __unicode__ return
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


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