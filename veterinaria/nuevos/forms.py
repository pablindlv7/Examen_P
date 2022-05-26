from django import forms
from .models import Nuevos

class FormularioNuevos(forms.ModelForm):
    class Meta:
        model=Nuevos
        fields= '__all__'