from django.db import models


class Inscripcion(models.Model):
    alumno = models.ForeignKey(
        'alumno.Alumno', on_delete=models.CASCADE, null=True, related_name='inscripciones'
    )
    cursada = models.ForeignKey(
        'cursada.Cursada', on_delete=models.CASCADE, null=True, related_name='inscripciones'
    )
    