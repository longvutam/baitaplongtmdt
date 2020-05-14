from django.urls import path
from .views import homeView, productView, checkoutView, product, add2Cart, cart
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('<int:product_id>/', views.product, name = "product"),
    path('add-to-cart/<int:product_id>/', views.add2Cart, name='add2Cart'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkoutView.as_view(), name = 'checkout'),
    path('removeall/', views.removeCart, name='removeCart'),
    path('ok/',views.checkout_ok, name = 'ok')
]