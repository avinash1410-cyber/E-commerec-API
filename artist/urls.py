from django.urls import path
from .views import Artist,ArtistAPIView

urlpatterns = [
    path('', ArtistAPIView.as_view(),name="artists"),
    path('<int:pk>/',ArtistAPIView.as_view()),

]