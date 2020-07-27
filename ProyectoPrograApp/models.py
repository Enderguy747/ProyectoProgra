from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Etiqueta(models.Model):
    nombreEtiqueta = models.CharField(max_length=45)

    def __str__(self):
        return self.nombreEtiqueta


class Foto(models.Model):
    url = models.CharField(max_length=45, primary_key=True)
    foto = models.ImageField(upload_to='')
    Etiqueta = models.ManyToManyField(Etiqueta)
    nombre = models.CharField(max_length=45)
    tipo = models.CharField(max_length=15)
    resolucion = models.CharField(max_length=15)
    privada = models.BooleanField()
    idUsuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return "url: {} - nombre: {} - Usuario: {} - visibilidad: {}".format(self.url,self.nombre,self.idUsuario,self.privada)
