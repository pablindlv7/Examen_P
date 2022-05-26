from django.shortcuts import render
from .models import Servicio

# Create your views here.

def lista(request):
     lista=Servicio.objects.all()

     return render(request, "lista/lista.html", {"lista": lista})
