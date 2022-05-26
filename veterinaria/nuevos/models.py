from django.db import models

# Create your models here.

class Nuevos(models.Model):
    Alimentacion= models.CharField(max_length=50)
    Vacunacion= models.CharField(max_length=50)
    Edad= models.CharField(max_length=10)
    Género= models.CharField(max_length=20)
    Nombre= models.CharField(max_length=50)
    Fecha_de_rescate= models.CharField(max_length=10)
    Adoptante= models.CharField(max_length=20)
    Raza= models.CharField(max_length=20)
    Alguna_Enfermedad= models.CharField(max_length=100)
