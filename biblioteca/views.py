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
        libro = Libro.objects.filter(pk=pk, disponibilidad="D").first()
        # También se puede hacer con libro = get_object_or_404(Libro, pk=pk)
        return render(request, "biblioteca/prestar_libro.html", {"libro": libro})

    def post(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        usuario = request.user  # Obtener el usuario actual
        libro.disponibilidad = "P"
        libro.save()
        Prestamo.objects.create(
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
        # context["prestamos"] = Prestamo.objects.all()

        context["prestamos"] = Prestamo.objects.filter(
            usuario=self.request.user, estado_prestamo="P", fecha_devolucion=None
        )  # Pongo la fecha de devolución a None para que solo me devuelva los libros que no han sido devueltos todavía

        context["prestamo_historial"] = Prestamo.objects.filter(
            usuario=self.request.user, estado_prestamo="D"
        )
        return context


class ListarDevueltos(ListView):
    model = Prestamo
    template_name = "biblioteca/listar_devueltos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # Esto es para que no se pise el contexto que ya tiene
        # context["prestamos"] = Prestamo.objects.all()
        context["prestamos"] = Prestamo.objects.filter(
            usuario=self.request.user, estado_prestamo="D"
        )

        return context


class DevolverLibro(View):
    def get(self, request, pk):
        libro = Libro.objects.filter(pk=pk, disponibilidad="P").first()
        return render(request, "biblioteca/devolver_libro.html", {"libro": libro})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk, disponibilidad="P")
        libro.disponibilidad = "D"
        libro.save()
        prestamo = Prestamo.objects.filter(
            libro_prestado=libro, usuario=request.user, estado_prestamo="P"
        ).first()  # Esto es para que solo devuelva el primer objeto que encuentre, ya que puede haber varios prestamos del mismo libro
        prestamo.fecha_devolucion = datetime.now()
        prestamo.estado_prestamo = "D"
        prestamo.save()
        return redirect("detalle_libro", pk=libro.pk)


class ValoracionLibro(View):
    def get(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        return render(request, "biblioteca/valoracion_libro.html", {"libro": libro})

    def post(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        libro.valoracion_media = request.POST[
            "valoracion"
        ]  # Esto es para que en el campo valoracion_media del libro se guarde la valoración que el usuario ha introducido en el formulario
        # En el formulario lo tengo que meter en un input de tipo number y con un name="valoracion"
        libro.save()
        return redirect("detalle_libro", pk=libro.pk)
