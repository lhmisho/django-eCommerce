from django.urls import path,re_path
from .views import cart_home

app_name = 'carts'

urlpatterns = [

    path('', cart_home,name='cart'),

]