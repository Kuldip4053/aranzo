"""
URL configuration for aranoz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from shop import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('profileupdate', views.profileupdate, name='profileupdate'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('wish', views.wish, name='wish'),
    path('search', views.search, name='search'),
    path('category', views.category, name='category'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('addtowishlist/<int:id>', views.addtowishlist, name='addtowishlist'),
    # path('checkout', views.checkout, name='checkout'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('feature', views.feature, name='feature'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('single_blog', views.single_blog, name='single_blog'),
    path('single_product/<int:id>', views.single_product, name='single_product'),
    path('tracking', views.tracking, name='tracking'),
    path('delete_file_in_folder', views.delete_file_in_folder, name='delete_file_in_folder'),
    path('qty_plus/<int:id>', views.qty_plus, name='qty_plus'),
    path('qty_minus/<int:id>', views.qty_minus, name='qty_minus'),
    path('wishremove/<int:id>', views.wishremove, name='wishremove'),
    path('cartremove/<int:id>', views.cartremove, name='cartremove'),
    path('single_cart/<int:id>', views.single_cart, name='single_cart'),
    path('reting', views.reting, name='reting'),
    path('forgot', views.forgot, name='forgot'),
    path('conform', views.conform, name='conform'),
    path('conf_password', views.conf_password, name='conf_password'),
    path('billingaddress', views.billingaddress, name='billingaddress'),
    path('check', views.check, name='check'),
    path('addressupdate/<int:id>', views.addressupdate, name='addressupdate'),
    path('addressdelete/<int:id>', views.addressdelete, name='addressdelete'),

    path('myorder', views.myorder, name='myorder'),





]
