# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# proof class imports
from .serializers import ShirtSerializer, UpdateShirtSerializer
from shirt.models import Shirt


class ShirtViewSet(ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateShirtSerializer
        return self.serializer_class
