from django.urls import path
from .views import ProductAPIView,CategoryView

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:pk>/', ProductAPIView.as_view()),
    path('cat/<slug:slug>/',CategoryView.as_view()),
]