from django.db import models


class GenericModel(models.Model):
    """Generic model to be inherited by all models."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Meta"""

        abstract = True
        ordering = ["-created_at"]
