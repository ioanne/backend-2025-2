from django.db import models


class Inscripcion(models.Model):
    fecha_inscripcion = models.DateField(auto_now_add=True)
    alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE)
    cursada = models.ForeignKey('cursada.Cursada', on_delete=models.CASCADE)

    def __str__(self):
        return f"Inscripcion {self.id} - Alumno: {self.alumno.nombre} {self.alumno.apellido} en Cursada {self.cursada.id}"