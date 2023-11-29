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

    # queryset = Libro.objects.filter(disponibilidad="D")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # Esto es para que no se pise el contexto que ya tiene
        context["libros_disponibles"] = Libro.objects.filter(
            disponibilidad="D"
        )  # Esto es para añadir un contexto nuevo
        context["libros_prestados"] = Libro.objects.filter(disponibilidad="P")
        return context


class CrearLibro(CreateView):
    model = Libro
    template_name = "biblioteca/crear_libro.html"
    fields = "__all__"
    success_url = reverse_lazy("listar_libros")


class DetalleLibro(DetailView):
    template_name = "biblioteca/detalle_libro.html"
    model = Libro


class EditarLibro(UpdateView):
    template_name = "biblioteca/editar_libro.html"
    model = Libro
    fields = "__all__"
    success_url = reverse_lazy("listar_libros")


class EliminarLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy("listar_libros")
