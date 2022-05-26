from django.db import models

# Create your models here.

class adopciones(models.Model):
    Nombre= models.CharField(max_length=50)
    Apellido= models.CharField(max_length=50)
    Edad= models.CharField(max_length=10)
    email= models.EmailField()
    Telefono= models.CharField(max_length=8)
    Domicilio= models.CharField(max_length=50)
    Numero_de_mascotas= models.CharField(max_length=10)
    Razones_para_adoptar= models.CharField(max_length=100)