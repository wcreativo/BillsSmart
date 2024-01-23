import asyncio
import csv

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.services import CSVExporter

from .services import ClientService, check_data_bulk_create


class ClientsReportView(APIView):
    async def get(self, request):
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

    async def post(self, request):
        if "file" not in request.FILES:
            return Response(
                {"error": "There is not a CSV file in the request."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        csv_file = request.FILES["file"]

        if not csv_file.name.endswith(".csv"):
            return Response(
                {"error": "The file must be CSV."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            with csv_file.open(mode="r") as file:
                decoded_file = csv_file.read().decode("utf-8").splitlines()
                csv_reader = csv.DictReader(decoded_file)
                data = list(csv_reader)
                success_bulk = await asyncio.to_thread(check_data_bulk_create, data)
                if success_bulk:
                    return Response(
                        {"message": "Bulk Create Clients Successfull"},
                        status=status.HTTP_200_OK,
                    )
                return Response(
                    {"error": "Bulk Create Clients Failed"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"error": f"Failed to process the CSV file. Error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response({"message": "CSV File processed successfully."})
