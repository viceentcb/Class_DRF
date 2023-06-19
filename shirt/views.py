# Django and DRF imports
import django_filters
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# proof class imports
from .serializers import (
    ListShirtSerializer,
    ListProfileShirtSerializer,
    UpdateShirtSerializer,
    CreateShirtSerializer
)
from shirt.models import Shirt


class ShirtViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ListShirtSerializer
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateShirtSerializer
        return self.serializer_class


class MeShirtView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = Shirt.objects.all()
    serializer_class = ListProfileShirtSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.queryset.filter(user_id=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdateShirtSerializer
        return self.serializer_class
