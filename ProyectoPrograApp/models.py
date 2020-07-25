from django.db import models

# Create your models here.


class Usuario(models.Model):
    idUsuario = models.CharField(max_length=20, primary_key=True)
    contraseña = models.CharField(max_length=45)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return 'Id:   {}' .format(self.idUsuario)


class Etiqueta(models.Model):
    nombreEtiqueta = models.CharField(max_length=45)

    def __str__(self):
        return self.nombreEtiqueta


class Foto(models.Model):
    url = models.CharField(max_length=45, primary_key=True)
    foto = models.ImageField()
    Etiqueta = models.ManyToManyField(Etiqueta)
    nombre = models.CharField(max_length=45)
    tipo = models.CharField(max_length=15)
    resolucion = models.CharField(max_length=15)
    privada = models.BooleanField()
    idUsuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    def __str__(self):
        return "url: {} - nombre: {} - Usuario: {} - visibilidad: {}".format(self.url,self.nombre,self.idUsuario,self.privada)
