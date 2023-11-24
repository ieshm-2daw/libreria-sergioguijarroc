from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Libro


admin.site.register(Usuario, UserAdmin, Libro)


# Register your models here.
