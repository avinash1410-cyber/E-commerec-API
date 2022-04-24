from django.urls import path
from .views import CustomerAPIView,login_page,logout_page


urlpatterns = [
    path('', CustomerAPIView.as_view()),
    path('<int:pk>/', CustomerAPIView.as_view()),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
]