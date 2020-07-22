from django.db import models

# Create your models here.


class Usuario(models.Model):
    idUsuario = models.CharField(max_length=20, primary_key=True)
    contraseña = models.CharField(max_length=45)
    correo = models.EmailField()

    def __str__(self):
        return "Id: %s - Contraseña:****** - correo: %s"(self.idUsuario, self.contraseña, self.correo)

class Etiqueta(models.Model):
    nombreEtiqueta = models.CharField(max_length=45)
    def __str__(self):
        return "Nombre: %s "(self.nombreEtiqueta)

class Foto(models.Model):
    url = models.CharField(max_length=45,primary_key=True)
    foto = models.ImageField()
    Etiqueta = models.ManyToManyField(Etiqueta)
    nombre = models.CharField(max_length=45)
    tipo = models.CharField(max_length=15)
    resolucion = models.CharField(max_length=15)
    privada = models.BooleanField()
    idUsuario = models.ForeignKey(Usuario,on_delete= models.DO_NOTHING)