from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('payment/', views.payment),
    path('response/', views.response),
]