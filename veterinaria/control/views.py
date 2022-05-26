from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

# Create your views here.

def inicio(request):
     return render(request, "control/inicio.html")


def vacunas(request):
     return render(request, "control/vacunas.html")

def registro(request):
     return render(request, "control/registro.html")






