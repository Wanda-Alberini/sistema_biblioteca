from django.contrib import admin
from django.urls import path

from biblioteca.views import (
    listar_lectores, listar_libros, archivar_libro, buscar_libros
)

# Son las URLS especificas de la app
urlpatterns = [
    path("lectores/", listar_lectores, name="lista_lectores"),
    path("libros/", listar_libros, name="lista_libros"),
    path("archivar-libro/", archivar_libro, name="archivar_libro"),
    path("buscar-libros/", buscar_libros, name="buscar_libros"),
]