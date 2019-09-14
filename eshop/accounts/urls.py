from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from .views import *
# from referrals import urls

app_name = 'accounts'
urlpatterns = [
    # authentication section
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest', guest_register_view, name='guest_register'),
    # url(r'^referrals/', include('referrals.urls', namespace='referrals')),
]
