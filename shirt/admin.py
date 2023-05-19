# Django and DRF imports
from django.contrib import admin

# proof class imports
from .models import Shirt


@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'color', 'phrase', 'emoji', 'created_at', 'updated_at', 'deleted_at', 'active')
    list_filter = ('color', 'stock')
    search_fields = ('name', 'phrase', 'emoji')
