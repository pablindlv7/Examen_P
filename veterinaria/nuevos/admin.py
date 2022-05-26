from django.contrib import admin
from .models import Nuevos

# Register your models here.

class nuevosAdmin(admin.ModelAdmin):
    list_display= ("Alimentacion", "Vacunacion", "Edad", "Nombre")
    search_fields= ("Nombre", "Edad")

admin.site.register(Nuevos, nuevosAdmin)

