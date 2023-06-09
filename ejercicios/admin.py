# Django and DRF imports
from django.contrib import admin

# proof class imports
from .models import Television, Nevera


@admin.register(Television)
class ShirtAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('__str__', 'id', 'pulgadas', 'numero_de_serie', 'created_at', 'updated_at', 'deleted_at', 'active')


@admin.register(Nevera)
class NeveraAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('__str__', 'id', 'vendido', 'created_at', 'updated_at', 'deleted_at', 'active')

