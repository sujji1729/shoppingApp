"""
URL configuration for ShoppyPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from .views import home, about, cart, checkOut, contact, productDetails, shop, wishlist, addproduct

urlpatterns = [
    
    path("", home, name="home"),
    path("about", about, name="about"),
    path("cart", cart, name="cart"),
    path("checkOut", checkOut, name="checkOut"),
    path("contact", contact, name="contact"),
    path("productDetails", productDetails, name="productDetails"),
    path("shop", shop, name="shop"),
    path("wishlist", wishlist, name="wishlist"),
    path("addproduct", addproduct, name="addproduct"),
]
