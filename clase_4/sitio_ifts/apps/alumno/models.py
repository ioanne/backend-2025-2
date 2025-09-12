from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"