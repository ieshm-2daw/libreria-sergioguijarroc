from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.


class Usuario(AbstractUser):
    dni = models.CharField(max_length=9, primary_key=True)
    direccion = models.TextField()
    telefono = models.IntegerField(validators=[MaxValueValidator(9)])


class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    biogafia = models.TextField()
    foto = models.ImageField()
    # A autor no le asignamos clave primaria ya que django por defecto le asigna un id que es autoincremental


class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey("Editorial", on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20)
    resumen = models.TextField()
    DISPONIBILIDAD = (
        ("D", "Disponible"),
        ("P", "Prestado"),
        ("E", "En proceso de préstamo"),
    )  # Esto es una tupla de tuplas (tupla anidada) para que el usuario solo pueda elegir entre las opciones que le damos
    portada = models.ImageField()


class Editorial(models.Model):
    nombre = models.CharField(max_length=15)
    direccion = models.TextField()
    sitio_web = models.URLField()


class Prestamo(models.Model):
    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado_prestamo = models.CharField(max_length=1, choices=Libro.DISPONIBILIDAD)
