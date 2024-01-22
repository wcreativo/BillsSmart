from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clients.models import Client
from apps.clients.serializers import ClientListSerializer, ClientSerializer


class ClientAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailAPIView(APIView):
    def get(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if not client:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ClientListSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if not client:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if not client:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        client.delete()
        return Response(
            {"message": "Client has been deleted successfully"},
            status=status.HTTP_200_OK,
        )
