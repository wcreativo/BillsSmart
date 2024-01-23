from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.bills.models import Bill
from apps.bills.serializers import BillSerializer


class BillAPIView(APIView):
    def get(self, request):
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillDetailAPIView(APIView):
    def get(self, request, pk):
        bill = Bill.objects.filter(id=pk).first()
        if not bill:
            return Response(
                {"error": "Bill not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        bill = Bill.objects.filter(id=pk).first()
        if not bill:
            return Response(
                {"error": "Bill not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bill = Bill.objects.filter(id=pk).first()
        if not bill:
            return Response(
                {"error": "Bill not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        bill.delete()
        return Response(
            {"message": "Bill has been deleted successfully"},
            status=status.HTTP_200_OK,
        )
