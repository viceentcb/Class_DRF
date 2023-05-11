# Django and DRF imports
from django.contrib import admin

# proof class imports
from .models import Shirt


@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'phrase', 'emoji', 'created_at', 'updated_at')
    list_filter = ('color', 'stock')
    search_fields = ('name', 'phrase', 'emoji')
