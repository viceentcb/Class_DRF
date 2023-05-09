# Django and DRF imports
from rest_framework import serializers

# proof class imports
from .models import Shirt


class ShirtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shirt
        fields = "__all__"
