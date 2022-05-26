from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from django.db import models

# Create your models here.

class Servicio(models.Model):
    mascota=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='servicios')
    alimentacion= models.CharField(max_length=50, null=True)
    edad= models.CharField(max_length=50, null=True)
    adoptante= models.CharField(max_length=50, null=True)
    raza= models.CharField(max_length=50, null=True)
    alguna_enfermedad= models.CharField(max_length=100, null=True)
    disponibilidad= models.BooleanField(default=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Lista'
        verbose_name_plural= 'Listas'

    def __str__(self):
        return self.mascota