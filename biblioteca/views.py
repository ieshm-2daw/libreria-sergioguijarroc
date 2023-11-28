from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Libro

# Create your views here.


class ListarLibros(ListView):
    model = Libro
    template_name = "biblioteca/listar_libros.html"


class CrearLibro(CreateView):
    model = Libro
    template_name = "biblioteca/crear_libro.html"
    fields = [
        "isbn",
        "autor",
        "editorial",
        "fecha_publicacion",
        "genero",
        "resumen",
        "disponibilidad",
    ]
    success_url = reverse_lazy("listar_libros")


class DetalleLibro(DetailView):
    template_name = "biblioteca/detalle_libro.html"
    model = Libro


class EditarLibro(UpdateView):
    template_name = "biblioteca/editar_libro.html"
    model = Libro
    fields = [
        "isbn",
        "autor",
        "editorial",
        "fecha_publicacion",
        "genero",
        "resumen",
        "disponibilidad",
    ]
    success_url = reverse_lazy("listar_libros")


class EliminarLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy("listar_libros")
