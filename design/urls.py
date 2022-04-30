from django.urls import path
from .views import Designs

urlpatterns = [
    path('', Designs.as_view()),
]