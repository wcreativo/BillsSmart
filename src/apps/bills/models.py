from django.db import models

from apps.clients.models import Client
from apps.core.models import GenericModel
from apps.products.models import Product


class Bill(GenericModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    products = models.ManyToManyField(
        Product, through="BillProduct", related_name="bills", blank=True
    )

    def __str__(self) -> str:
        return f"{self.code}"


class BillProduct(GenericModel):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
