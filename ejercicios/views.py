# Django and DRF imports
from rest_framework.viewsets import ModelViewSet

# proof class imports
from ejercicios.models import Television
from ejercicios.serializers import TelevisionSerializer


class TelevisionViewSet(ModelViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'numero_de_serie'


class NeveraViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.Update, GenericViewSet):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializer
    lookup_field = 'id'

