from django.db import models

from apps.clients.models import Client
from apps.core.models import GenericModel
from apps.products.models import Product


class Bill(GenericModel):
    cliend_id = models.ManyToManyField(Client, related_name="bills")
    company_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    products = models.ManyToManyField(
        Product, through="BillProduct", related_name="bills"
    )

    def __str__(self) -> str:
        return f"{self.code}"


class BillProduct(GenericModel):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
