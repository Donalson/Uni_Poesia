from datetime import datetime
from django.db import models

# Create your models here.
@classmethod
def hoy():
    x = str(datetime.now())[0:10]
    return x

class PoesiaManager(models.Manager):
    def crear_poesia(self, carnet, nombre, direccion, telefono, genero, fnacimiento, carrera, generop, finscripcion, fdeclamacion):
        print(carnet, nombre, direccion, telefono, genero, fnacimiento, carrera, generop, finscripcion, fdeclamacion)
        poesia = self.create(Carnet= carnet, Nombre_Completo=nombre, Direccion=direccion, Genero=genero, Telefono=telefono, Fecha_Nacimiento=fnacimiento, Carrera_Estudiante=carrera, Genero_Poesia=generop, Fecha_Inscripcion=finscripcion, Fecha_Declamacion=fdeclamacion)
        return poesia

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

    objects = PoesiaManager()