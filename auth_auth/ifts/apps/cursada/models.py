from django.db import models

from datetime import datetime

class Cursada(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(null=True, blank=True)
    profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE)

    def __str__(self):
        return f"Cursada {self.id} - Profesor: {self.profesor.nombre} {self.profesor.apellido}"
