# dj_razorpay/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='index'),
	path('pay/', views.paymenthandler, name='paymenthandler'),
]