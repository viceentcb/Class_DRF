# Django and DRF imports
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# proof class imports
from ejercicios.models import Television
from ejercicios.serializers import TelevisionSerializer


class TelevisionViewSet(ModelViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'numero_de_serie'


class NeveraViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'id'

