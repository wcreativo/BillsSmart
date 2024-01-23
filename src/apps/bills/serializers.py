from rest_framework import serializers

from apps.clients.models import Client
from apps.products.models import Product

from .models import Bill, BillProduct


class BillSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField(max_length=255)
    nit = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True
    )

    def create(self, validated_data):
        products = validated_data.pop("products")
        bill = Bill.objects.create(**validated_data)
        bill.products.set(products)
        return bill

    def update(self, instance, validated_data):
        BillProduct.objects.filter(bill_id=instance.id).delete()
        products = validated_data.pop("products")
        instance.company_name = validated_data["company_name"]
        instance.nit = validated_data["nit"]
        instance.code = validated_data["code"]
        instance.client = validated_data["client"]
        instance.products.set(products)
        return instance
