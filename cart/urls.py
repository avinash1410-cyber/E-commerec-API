from django.urls import path
from .views import CartAPIView

urlpatterns = [
    path('', CartAPIView.as_view()),
    path('<int:pk>/',CartAPIView.as_view()),

]