from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import usuarioFormulario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def VRegistro(request):
     data={
        'form':usuarioFormulario()
     }
     if request.method=='POST':
          formulario=usuarioFormulario(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
               login(request, user)
               messages.success(request, "Te has registrado correctamente")
               #Redireccionar al Home
     
               return redirect(to="Inicio")

          else:
               for msg in formulario.error_messages:
                    messages.error(request, formulario.error_messages[msg])
               return render(request, "usuario/uduario.html",{"form":formulario})
     return render(request, 'usuario/usuario.html', data)

def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')




def logear(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")
            
    form=AuthenticationForm()
    return render(request, "usuario/login.html",{"form":form})

