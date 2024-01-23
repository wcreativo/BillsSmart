from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.services import CSVExporter

from .services import ClientService


class ClientsReportView(APIView):
    def get(self, request):
        data = ClientService.total_bills_by_client()
        if data:
            field_names = ["document", "full_name", "total_bills"]
            csv_file = CSVExporter.export_to_csv(data, field_names)
            if csv_file:
                with open("output.csv", "r") as f:
                    contenido = f.read()

                    response = HttpResponse(contenido, content_type="text/csv")
                    response[
                        "Content-Disposition"
                    ] = 'attachment; filename="output.csv"'

                    return response
            return Response(
                {"message": "There's not file to export"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "There're not clients on database"},
            status=status.HTTP_400_BAD_REQUEST,
        )
