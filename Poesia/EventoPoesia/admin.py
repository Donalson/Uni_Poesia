from django.contrib import admin
from .models import Poesia

# Register your models here.

class PoesiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'Carnet', 'Nombre_Completo']
    ordering = ['id']

admin.site.register(Poesia, PoesiaAdmin)
