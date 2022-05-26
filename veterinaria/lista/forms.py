from dataclasses import fields
from django import forms
from .models import Servicio

class VistaForms(forms.ModelForm):
    class Meta: 
        model=Servicio
        fields= ["mascota", "descripcion", "imagen", "alimentacion", "edad", "raza"]