# Django and DRF imports
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
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

    def get_permissions(self):
        if self.action in ('create', 'favorite', 'unfavorite'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

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

    @action(detail=True, methods=['POST'])
    def favorite(self, request, id):
        shirt = self.get_object()
        self.request.user.do_favorite(shirt)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def unfavorite(self, request, id):
        shirt = self.get_object()
        self.request.user.do_unfavorite(shirt)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
