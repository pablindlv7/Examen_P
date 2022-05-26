from django import forms
from .models import adopciones

class FormularioAdopciones(forms.ModelForm):
    class Meta:
        model=adopciones
        fields= '__all__'

    

