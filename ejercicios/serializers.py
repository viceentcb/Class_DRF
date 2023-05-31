# Django and DRF imports
from rest_framework import serializers

# proof class imports
from ejercicios.models import Television


class TelevisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Television
        fields = "__all__"


    def create(self, data):
        Television(**data)
        Television.save()

    def update(self, data):  #PUT

        objeto.pulgadas = data["pulgadasa"]
        objeto.numero_de_serie = "numero_de_serie"

        objeto.save()



class TelevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Television
        fields = "__all__"

    def create(self, data):
        Nevera(anchura="5", altura="2", color="negro")
        Nevera.save()

    def update(self, data): #Patch
        objeto.altura = data["altura"]
        objeto.color = "color"
        objeto.anchura = "anchura"

        objeto.save("anchura", "altura")
