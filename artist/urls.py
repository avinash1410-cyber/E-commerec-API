from django.urls import path
from .views import Artist,ArtistAPIView,ArtistDesignAPIView

urlpatterns = [
    path('', ArtistAPIView.as_view(),name="artists"),
    path('<int:pk>/',ArtistAPIView.as_view()),
    path('<int:pk>/designs/',ArtistDesignAPIView.as_view()),
]