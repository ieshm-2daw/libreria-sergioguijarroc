from .views import ListarLibros, CrearLibro, DetalleLibro, EditarLibro, EliminarLibro
from django.urls import path

urlpatterns = [
    path("", ListarLibros.as_view(), name="listar_libros"),
    path("crear/", CrearLibro.as_view(), name="crear_libro"),
    path("detalle/<int:pk>", DetalleLibro.as_view(), name="detalle_libro"),
    path("editar/<int:pk>", EditarLibro.as_view(), name="editar_libro"),
    path("eliminar/<int:pk>", EliminarLibro.as_view(), name="eliminar_libro"),
]
