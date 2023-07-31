from django.contrib import admin

# Register your models here.


from biblioteca.models import Libro, Lector, Prestamo


admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Prestamo)
