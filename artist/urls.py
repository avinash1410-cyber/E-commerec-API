from django.urls import path
from .views import Artist,ArtistAPIView

urlpatterns = [
    path('', ArtistAPIView.as_view()),
    path('<int:pk>/',ArtistAPIView.as_view()),

]