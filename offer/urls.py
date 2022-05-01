from django.urls import path
from .views import offers
urlpatterns = [
    path('<int:pk>/',offers),
]