from django.shortcuts import render
from django.contrib import messages
from lista.forms import VistaForms


# Create your views here.


def nuevos(request):
    data={
        'form': VistaForms()
    }
    if request.method=='POST':
        formulario=VistaForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud enviada")
        else:
            data["form"]=formulario

    return render(request, "nuevos/nuevos.html",data)