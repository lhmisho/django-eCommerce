"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,re_path, include

from address.views import checkout_address_created_view,checkout_address_reuse_view
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),

    # including products app
    path('', include('products.urls')),

    # including login apps
    path('', include('accounts.urls')),

    # including search app
    path('search/', include('search.urls')),

    # including carts app
    path('cart/', include('carts.urls')),
    # authentication section
    path('contact/', contact_page, name='contact'),

    # mapping address view
    path('checkout_address_created_view/', checkout_address_created_view, name='checkout_address_created'),
    path('checkout/address/reuse/view/', checkout_address_reuse_view, name='checkout_address_reuse'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)