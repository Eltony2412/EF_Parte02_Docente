from django.db import models

# Create your models here.
class Docente(models.Model):
    codigo = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado =models.CharField( max_length=1)


