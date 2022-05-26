from django import forms

class FormularioContacto(forms.Form):

    usuario= forms.CharField(label="Usuario", required=True)

    email= forms.CharField(label="Email", required=True)

    contenido= forms.CharField(label="Contenido", widget=forms.Textarea)