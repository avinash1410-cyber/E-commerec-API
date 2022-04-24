from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('', OrderAPIView.as_view()),
    path('<int:pk>/',OrderAPIView.as_view()),
]