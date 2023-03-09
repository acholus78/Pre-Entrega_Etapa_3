from django.db import models

# Create your models here.
class Producto (models.Model): #Hereda de models.Model
	id=models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=40)
	anio_fabricacion = models.IntegerField ()
	descripcion = models.CharField (max_length=50)
	precio = models.CharField (max_length=50)


class Proveedor (models.Model): 
	nombre= models.CharField (max_length=30)
	apellido = models.CharField (max_length=30)
	email = models.EmailField()


class Cliente (models.Model):
	nombre = models.CharField (max_length=30)
	apellido = models.CharField (max_length=30)
	email = models.EmailField()
	direccion = models.CharField (max_length=30)





