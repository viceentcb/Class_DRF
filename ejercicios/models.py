from django.db import models
import uuid

from utils.models import BaseModel


class Television(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pulgadas = models.PositiveIntegerField()
    numero_de_serie = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # return "Hola"
        return f" Television: {self.numero_de_serie}"


class Nevera(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    anchura = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100, default="Proof")
    marca = models.CharField(max_length=100, null=True, blank=True)
    vendido = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"Nevera de color {self.color}"

class Comentario(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publicacion = models.IntegerField()
    usuario = models.CharField(max_length=100)
    comentario = models.CharField(max_length=1000)

    def __str__(self):
        return f"user {self.usuario}: publicacion {self.publicacion}"