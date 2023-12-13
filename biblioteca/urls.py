from .views import (
    ListarLibros,
    CrearLibro,
    DetalleLibro,
    EditarLibro,
    EliminarLibro,
    PrestarUnLibro,
    ListarPrestamos,
    ListarDevueltos,
    DevolverLibro,
    ValoracionLibro,
)
from django.urls import path

urlpatterns = [
    path("", ListarLibros.as_view(), name="listar_libros"),
    path("crear/", CrearLibro.as_view(), name="crear_libro"),
    path("detalle/<int:pk>", DetalleLibro.as_view(), name="detalle_libro"),
    path("editar/<int:pk>", EditarLibro.as_view(), name="editar_libro"),
    path("eliminar/<int:pk>", EliminarLibro.as_view(), name="eliminar_libro"),
    path("prestar/<int:pk>", PrestarUnLibro.as_view(), name="prestar_libro"),
    path("prestamos/", ListarPrestamos.as_view(), name="listar_prestamos"),
    path("devueltos/", ListarDevueltos.as_view(), name="listar_devueltos"),
    path("devolver/<int:pk>", DevolverLibro.as_view(), name="devolver_libro"),
    path("valoracion/<int:pk>", ValoracionLibro.as_view(), name="valoracion_libro"),
]
