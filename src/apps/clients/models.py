from django.db import models

from apps.core.models import GenericModel


class Client(GenericModel):
    document = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
