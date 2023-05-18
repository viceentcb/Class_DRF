# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# proof class imports
from .serializers import ListShirtSerializer, UpdateShirtSerializer, CreateShirtSerializer
from shirt.models import Shirt


class ShirtViewSet(ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ListShirtSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateShirtSerializer
        elif self.action == "create":
            return CreateShirtSerializer
        return self.serializer_class
