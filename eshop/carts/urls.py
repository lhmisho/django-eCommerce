from django.urls import path,re_path
from .views import *

app_name = 'cart'

urlpatterns = [

    path('', cart_home,name='home'),
    path('checkout/', checkout_home,name='checkout'),
    path('update/', cart_update,name='update'),

]