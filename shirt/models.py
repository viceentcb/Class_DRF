# Python imports
import uuid

# Django and DRF imports
from django.db import models

# proof class imports
from utils.models import BaseModel
from authentication.models import User


class ColorType(models.TextChoices):
    RED = 'R', 'Rojo'
    BLUE = 'A', 'Azul'
    YELLOW = 'Am', 'Amarillo'
    BLACK = 'N', 'Negro'
    BROWN = 'M', 'Marron'
    WHITE = 'B', 'Blanco'

    @classmethod
    def get_all_choices(cls):
        return {choice.value: choice.label for choice in cls}


class Shirt(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=50, choices=ColorType.choices)
    stock = models.IntegerField()
    phrase = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "T-Shirt"
        verbose_name_plural = "TShirts"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}"

    def is_favorite(self, user):
        return self.favorites_by.filter(id=user.id).exists()

    def favorites(self):
        return self.favorites_by.count()

