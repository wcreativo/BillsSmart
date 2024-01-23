from django.urls import path

from .views import ClientsReportView

urlpatterns = [
    path("client-bills/", ClientsReportView.as_view(), name="client-bills"),
]
