from django.urls import path

from lista import views

urlpatterns = [
    
    path('', views.lista, name="Lista"),
]