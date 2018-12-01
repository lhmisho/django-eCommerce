from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

app_name = 'accounts'
urlpatterns = [
    # authentication section
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest', guest_register_view, name='guest_register'),
]
