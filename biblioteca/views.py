from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from biblioteca.models import Libro, Lector
from biblioteca.forms import LibroFormulario


def listar_lectores(request):
    contexto = {
        
        "lectores": Lector.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='biblioteca/lista_lectores.html',
        context=contexto,
    )
    return http_response

def listar_libros(request):
    
    contexto = {
        "libros": Libro.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='biblioteca/lista_libros.html',
        context=contexto,
    )
    return http_response



    
    
def archivar_libro_version_1(request):
    
    if request.method == "POST": 
        data = request.POST  
        autor = data['autor']
        titulo = data['titulo']
        
        libro = Libro(libro=libro, titulo=titulo)
        
        libro.save()

        
        url_exitosa = reverse('lista_libros')
        return redirect(url_exitosa)
    else:  
        http_response = render(
            request=request,
            template_name='biblioteca/formulario_libro_a_mano.html',
        )
        return http_response
    
    
    
    
def archivar_libro(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = LibroFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            autor = data["autor"]
            titulo = data["titulo"]
            # creo un curso en memoria RAM
            libro = Libro(autor=autor, titulo=titulo)
            # Lo guardan en la Base de datos
            libro.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_libros')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = LibroFormulario()
    http_response = render(
        request=request,
        template_name='biblioteca/formulario_libro.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_libros(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        libros = Libro.objects.filter(titulo__contains=busqueda)
        contexto = {
            "libros": libros,
        }
        http_response = render(
            request=request,
            template_name='biblioteca/lista_libros.html',
            context=contexto,
        )
        return http_response
    else:  # Método GET
        # Obtener todos los libros para mostrar la lista completa al acceder directamente a la URL
        libros = Libro.objects.all()
        contexto = {
            "libros": libros,
        }
        http_response = render(
            request=request,
            template_name='biblioteca/lista_libros.html',
            context=contexto,
        )
        return http_response