from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

app_name = 'accounts'
urlpatterns = [
    # authentication section
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', register_page, name='register'),
]
