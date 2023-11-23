from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.


class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    direccion = models.TextField()
    telefono = models.IntegerField(validators=[MaxValueValidator(9)])


class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20)
    resumen = models.TextField()
    DISPONIBILIDAD = (
        ("D", "Disponible"),
        ("P", "Prestado"),
        ("E", "En proceso de préstamo"),
    )
    portada = models.ImageField()


class Autor(models.Model):
    nombre = models.CharField(primary_key=True)
    biogafia = models.TextField()
    foto = models.ImageField()


class Editorial(models.Model):
    nombre = models.CharField(max_length=15)
