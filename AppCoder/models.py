from django.db import models

# Create your models here.
class Producto (models.Model): #Hereda de models.Model
	id=models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=40)
	anio_fabricacion = models.IntegerField ()
	descripcion = models.CharField (max_length=50)
	precio = models.CharField (max_length=50)

	def __str__(self):
		return f"Nombre:{self.nombre} - Año Fabricacion:{self.anio_fabricacion} - descripcion:{self.descripcion} - precio:{self.precio}"

class Proveedor (models.Model): 
	nombre= models.CharField (max_length=30)
	apellido = models.CharField (max_length=30)
	email = models.EmailField()

	def __str__(self):
		return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email:{self.email}"

class Cliente (models.Model):
	nombre = models.CharField (max_length=30)
	apellido = models.CharField (max_length=30)
	email = models.EmailField()
	direccion = models.CharField (max_length=30)

	def __str__(self):
		return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email:{self.email} - Direccion: {self.direccion}"



