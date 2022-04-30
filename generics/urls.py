from django.contrib import admin
from django.urls import path, include
from .views import search,get_products_by_date

urlpatterns = [
    #path('',search,name="home"),
    path('',get_products_by_date,name="home"),
    path('admin/', admin.site.urls,name="login"),
    path('api/', include('api.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
    path('category/', include('category.urls')),
    path('checkout/', include('checkout.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('artist/', include('artist.urls')),
    path('pay/', include('paytm.urls')),
    path('designs/', include('design.urls')),
]