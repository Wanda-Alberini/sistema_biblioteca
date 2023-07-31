from django.db import models

# Create your models here.

class Libro(models.Model):
    # los atributos de clase (son las columnas de la tabla)
    autor= models.CharField(max_length=64)
    titulo = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.autor},{self.titulo}"

class Lector(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre},{self.apellido}"


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f'{self.lector} - {self.libro}'