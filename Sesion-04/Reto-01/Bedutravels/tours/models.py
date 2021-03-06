from django.db import models

# Create your models here.
class User(models.Model):
    """ Define la tabla User """
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    clave = models.CharField(max_length=40, null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para User """
        return "{} {}".format(self.nombre, self.apellidos)


class Zona(models.Model):
    """ Define la tabla Zona """
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para Zona """
        return "{}".format(self.nombre)
