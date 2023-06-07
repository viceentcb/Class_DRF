# Django and DRF imports
import django_filters
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# proof class imports
from ejercicios.models import Television, Nevera
from ejercicios.serializers import TelevisionSerializer, NeveraSerializer


class TelevisionViewSet(ModelViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'numero_de_serie'


class NeveraViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Nevera.objects.all()
    serializer_class = NeveraSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = {
        "marca": ["icontains", "isnull", "exact", "in"],
        "altura": ["lt", "lte", "exact", "gte", "gt", "in"],
        "nombre": ["icontains"],
        "vendido": ["exact", "isnull"]

    }

    search_fields = ['color', "nombre"]
    ordering_fields = "__all__"
