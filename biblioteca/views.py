from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Libro, Prestamo
from django.views import View

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


class PrestarUnLibro(View):
    def get(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        # También se puede hacer con libro = get_object_or_404(Libro, pk=pk)
        return render(request, "biblioteca/prestar_libro.html", {"libro": libro})

    def post(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        usuario = request.user  # Obtener el usuario actual
        libro.disponibilidad = "P"
        libro.save()
        prestamo = Prestamo.objects.create(
            libro_prestado=libro,
            fecha_prestamo=datetime.now(),
            fecha_devolucion=None,
            usuario=usuario,  # Asignar el usuario al objeto Prestamo
            estado_prestamo="P",
        )
        return redirect("detalle_libro", pk=libro.pk)


class ListarPrestamos(ListView):
    model = Prestamo
    template_name = "biblioteca/listar_prestamos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # Esto es para que no se pise el contexto que ya tiene
        context["prestamos"] = Prestamo.objects.all()
        return context


class ListarDevueltos(ListView):
    model = Prestamo
    template_name = "biblioteca/listar_devueltos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # Esto es para que no se pise el contexto que ya tiene
        context["prestamos"] = Prestamo.objects.all()
        return context


class DevolverLibro(View):
    def get(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        return render(request, "biblioteca/devolver_libro.html", {"libro": libro})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.disponibilidad = "D"
        libro.save()
        prestamo = Prestamo.objects.filter(
            libro_prestado=libro, usuario=request.user
        ).first()
        prestamo.fecha_devolucion = datetime.now()
        prestamo.estado_prestamo = "D"
        prestamo.save()
        return redirect("detalle_libro", pk=libro.pk)
