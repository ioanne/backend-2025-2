from django.db import models


class Cursada(models.Model):
    materia = models.ForeignKey(
        'materia.Materia', on_delete=models.CASCADE, null=True, related_name='cursadas'
    )
    profesor = models.ForeignKey(
        'profesor.Profesor', on_delete=models.CASCADE, null=True, related_name='cursadas'
    )
    año = models.IntegerField(null=True, blank=True)
    cuatrimestre = models.IntegerField(null=True, blank=True)
