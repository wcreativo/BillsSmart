from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.models import Product
from apps.products.serializers import ProductListSerializer, ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        if not product:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductListSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        if not product:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        if not product:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        product.delete()
        return Response(
            {"message": "Product has been deleted successfully"},
            status=status.HTTP_200_OK,
        )
