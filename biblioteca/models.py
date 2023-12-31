from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db.models import Avg


class Usuario(AbstractUser):
    dni = models.CharField(max_length=9, unique=True, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.IntegerField(
        validators=[MaxValueValidator(9)], null=True, blank=True
    )
    prestamo_actual = models.ForeignKey(
        "Prestamo",
        on_delete=models.CASCADE,
        blank=True,
        related_name="prestamos_usuario",
        null=True,
    )


class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    biografia = models.TextField()  # Corregí el nombre del campo
    foto = models.ImageField()


class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=50)
    autor = models.ManyToManyField(Autor, blank=True)
    editorial = models.ForeignKey(
        "Editorial", blank=True, null=True, on_delete=models.CASCADE
    )  # Corregí el nombre del campo
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20)
    resumen = models.TextField()
    DISPONIBILIDAD = [
        ("D", "Disponible"),
        ("P", "Prestado"),
    ]
    disponibilidad = models.CharField(max_length=1, choices=DISPONIBILIDAD, default="D")
    portada = models.ImageField(upload_to="portadas/", null=True, blank=True)
    valoracion_media = models.FloatField(blank=True, null=True, default=None)

    def actualizar_valoracion_media(self):
        # Obtengo todas las valoraciones asociadas al libro
        reviews = Valoracion.objects.filter(prestamo_valoracion__libro_prestado=self)

        # Calculo el promedio de las valoraciones
        avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"]
        # Actualizo la valoración media del libro
        if avg_rating is not None:
            self.valoracion_media = avg_rating

        # Guardo el libro actualizado
        self.save()


class Editorial(models.Model):
    nombre = models.CharField(max_length=15)
    direccion = models.TextField()
    sitio_web = models.URLField()
    # libros = models.ForeignKey(Libro, blank=True, on_delete=models.CASCADE)  # No es necesario tener esta relación aquí


# Cambios
class Prestamo(models.Model):
    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="prestamos_usuario"
    )  # Related name es para que no se pise con el nombre de la clase y se pueda acceder a los prestamos de un usuario
    DISPONIBILIDAD = [
        ("D", "Devuelto"),
        ("P", "Prestado"),
    ]
    estado_prestamo = models.CharField(max_length=1, choices=DISPONIBILIDAD)
    # valoracion_usuario = models.FloatField(blank=True, null=True, default=None)
    valoracion_usuario = models.OneToOneField(
        "Valoracion", on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    numero_valoraciones = models.IntegerField(blank=True, null=True, default=0)


class Valoracion(models.Model):
    prestamo_valoracion = models.OneToOneField(Prestamo, on_delete=models.CASCADE)
    usuario_valoracion = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
    )
    rating = models.FloatField(null=True, blank=True, default=None)

    def actualizar_rating(self, rating):
        self.rating = rating
