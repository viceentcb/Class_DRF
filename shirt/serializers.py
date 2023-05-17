# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import Shirt


class ShirtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shirt
        fields = "__all__"


class UpdateShirtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shirt
        fields = "__all__"
        read_only_fields = ["id", "color", "phrase", "emoji"]
