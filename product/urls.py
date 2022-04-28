from django.urls import path
from .views import ProductAPIView,CategoryView,Home

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:pk>/', ProductAPIView.as_view()),
    path('cat/<slug:slug>/',CategoryView.as_view()),
    path('trend/',Home.as_view()),
    path('trend/',Home.as_view()),
]