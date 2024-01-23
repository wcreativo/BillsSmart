from django.urls import path

from .views import BillAPIView, BillDetailAPIView

urlpatterns = [
    path("", BillAPIView.as_view(), name="bill-list"),
    path("<int:pk>/", BillDetailAPIView.as_view(), name="bill-detail"),
]
