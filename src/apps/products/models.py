from django.db import models

from apps.core.models import GenericModel


class Product(GenericModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
