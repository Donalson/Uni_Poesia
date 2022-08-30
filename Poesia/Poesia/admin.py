from django.contrib import admin
from .models import Poesia

# Register your models here.

class PoesiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Poesia, PoesiaAdmin)