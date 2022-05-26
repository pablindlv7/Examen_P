from django.shortcuts import render
from adopciones.forms import FormularioAdopciones
from django.contrib import messages

# Create your views here.


def adopciones(request):
    data={
        'form': FormularioAdopciones()
    }
    if request.method=='POST':
        formulario=FormularioAdopciones(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud enviada")
        else:
            data["form"]=formulario

    return render(request, "adopciones/adopciones.html",data)