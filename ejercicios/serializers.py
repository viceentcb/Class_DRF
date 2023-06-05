# Django and DRF imports
from rest_framework import serializers

# proof class imports
from ejercicios.models import Television, Nevera


class TelevisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Television
        fields = "__all__"

    def create(self, validated_data):
        television = Television(**validated_data)
        television.save()

        return television

    def update(self, instance, validated_data):  #PUT

        instance.pulgadas = validated_data["pulgadas"]
        instance.numero_de_serie = validated_data["numero_de_serie"]

        instance.save(update_fields=["pulgadas", "numero_de_serie"])

        return instance


class NeveraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nevera
        fields = "__all__"

