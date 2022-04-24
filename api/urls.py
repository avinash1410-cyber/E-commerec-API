from django.urls import path,include
from .views import OrderAPIView

urlpatterns = [
    path('', OrderAPIView.as_view()),
    path('<int:pk>/',OrderAPIView.as_view()),
    # path('login/', userlogin, name="login"),
]