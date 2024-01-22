from django.urls import path

from .views import ClientAPIView, ClientDetailAPIView

urlpatterns = [
    path("", ClientAPIView.as_view(), name="client-list"),
    path("<int:pk>/", ClientDetailAPIView.as_view(), name="client-detail"),
]
