from datetime import datetime
from django.db import models

# Create your models here.
@classmethod
def hoy():
    x = str(datetime.now())[0:10]
    return x

class Poesia(models.Model):
    Generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    Generos_Poesia = (
        ('L', 'Lírica'),
        ('E', 'Épica'),
        ('D', 'Dramática')
    )

    Carnet = models.CharField(max_length=6)
    Nombre_Completo = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=30)
    Genero = models.CharField(max_length=1, choices=Generos)
    Telefono = models.CharField(max_length=15)
    Fecha_Nacimiento = models.DateField()
    Carrera_Estudiante = models.CharField(max_length=50)
    Genero_Poesia = models.CharField(max_length=1, choices=Generos_Poesia)
    Fecha_Inscripcion = models.DateField(default=hoy)
    Fecha_Declamacion = models.DateField()