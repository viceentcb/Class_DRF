# Django and DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# proof class imports
from .serializers import ListShirtSerializer, UpdateShirtSerializer, CreateShirtSerializer
from shirt.models import Shirt


class ShirtViewSet(ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ListShirtSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action in ["partial_update", "update"]:
            return UpdateShirtSerializer
        elif self.action == "create":
            return CreateShirtSerializer
        return self.serializer_class
