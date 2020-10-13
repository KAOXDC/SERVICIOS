from django.db import models


# Create your models here.
class Categoria(models.Model):
	nombre			= models.CharField(max_length = 100)
	descripcion		= models.TextField(max_length = 500)
	
	def __str__ (self):
		return self.nombre

class Marca (models.Model):
	nombre			= models.CharField(max_length = 100)

	def __str__ (self):
		return self.nombre

class Producto (models.Model):

	nombre			= models.CharField(max_length = 100)
	descripcion		= models.TextField(max_length = 500)
	status			= models.BooleanField(default = True)
	precio			= models.DecimalField(max_digits = 6, decimal_places = 2)
	stock			= models.IntegerField()
	categorias		= models.ManyToManyField(Categoria, null = True, blank = True)
	marca 			= models.ForeignKey(Marca, on_delete=models.PROTECT)
	foto 			= models.ImageField(upload_to='fotos', null=True, blank=True)

	def __str__ (self):
		return self.nombre


from django.contrib.auth.models import User

class Perfil (models.Model):
	user 	= models.OneToOneField(User, on_delete=models.CASCADE)
	foto 	= models.ImageField(upload_to='perfiles', null=True, blank=True)
	celular	= models.CharField(max_length = 100, blank=True)

class Persona(models.Model):
	nombre = models.CharField(max_length=25)
	password= models.CharField(max_length=25)

	def __str__ (self):
		return self.nombre

	class Meta:
		permissions = (
			('administrador','administrador'),
			('cliente','cliente'),
		)

