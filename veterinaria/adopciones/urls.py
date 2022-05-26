from django.urls import path

from adopciones import views

urlpatterns = [

    path('', views.adopciones, name="Adopciones"),
    
]