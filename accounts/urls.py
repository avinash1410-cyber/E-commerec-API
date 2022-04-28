from django.urls import path
from .views import CustomerAPIView,login_page,logout_page,register_page,update_artist


urlpatterns = [
    path('', CustomerAPIView.as_view()),
    path('<int:pk>/', CustomerAPIView.as_view()),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('register/', register_page, name="register"),
    path('update/', update_artist, name="update"),
]