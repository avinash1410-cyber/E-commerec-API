from django.urls import path
from .views import CheckAPIView

urlpatterns = [
    path('', CheckAPIView.as_view()),
    path('<int:pk>/',CheckAPIView.as_view()),

]