from django.db import models


# Create your models here.
class usuario(models.Model):
    idusuario=models.IntegerField(primary_key=True, verbose_name='id usuario')
    nombreusuario=models.CharField(max_length=50)
    apellidousuario=models.CharField(max_length=50)
    correo=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=30)
    


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'






opciones_consultas =[
    [0,"consultas"],
    [1,"reclamos"],
    [2,"sugerencias"],
    [3,"otros"],



]


class formulario(models.Model):
    nombre= models.CharField(max_length=50)
    correo= models.EmailField()
    tipo_consulta= models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre

