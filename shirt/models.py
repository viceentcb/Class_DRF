# Python imports
import uuid

# Django and DRF imports
from django.db import models

# proof class imports
from utils.models import TimestampedModel


class Shirt(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=50)
    stock = models.IntegerField()
    phrase = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "T-Shirt"
        verbose_name_plural = "TShirts"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"
