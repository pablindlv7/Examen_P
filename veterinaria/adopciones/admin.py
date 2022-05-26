from django.contrib import admin
from .models import adopciones

# Register your models here.

class nuevosAdopciones(admin.ModelAdmin):
    list_display= ("Nombre", "Telefono", "email", "Apellido")
    search_fields= ("Nombre", "email")

admin.site.register(adopciones, nuevosAdopciones)
