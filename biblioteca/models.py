from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.


class Usuario(AbstractUser):
    dni = models.CharField(max_length=9, unique=True, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.IntegerField(
        validators=[MaxValueValidator(9)], null=True, blank=True
    )
    Prestamo = models.ForeignKey("Prestamo", on_delete=models.CASCADE, blank=True)


class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    biogafia = models.TextField()
    foto = models.ImageField()
    # A autor no le asignamos clave primaria ya que django por defecto le asigna un id que es autoincremental


class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor, blank=True)
    Editorial = models.ForeignKey("Editorial", blank=True, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20)
    resumen = models.TextField()
    DISPONIBILIDAD = (
        ("D", "Disponible"),
        ("P", "Prestado"),
        ("E", "En proceso de préstamo"),
    )  # Esto es una tupla de tuplas (tupla anidada) para que el usuario solo pueda elegir entre las opciones que le damos
    disponibilidad = models.CharField(max_length=20, choices=DISPONIBILIDAD)
    portada = models.ImageField(upload_to="portadas/", null=True, blank=True)


# )  # Se crea en una carpeta portadas que se mete dentro de nuestra carpeta MEDIA definida en el settings.py


class Editorial(models.Model):
    nombre = models.CharField(max_length=15)
    direccion = models.TextField()
    sitio_web = models.URLField()
    Libros = models.ForeignKey(Libro, blank=True, on_delete=models.CASCADE)


class Prestamo(models.Model):
    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    DISPONIBILIDAD = (
        ("D", "Disponible"),
        ("P", "Prestado"),
    )
    estado_prestamo = models.CharField(max_length=1, choices=DISPONIBILIDAD)
