from django.db import models


class Cursada(models.Model):
    año = models.IntegerField(null=True, blank=True)
    cuatrimestre = models.IntegerField(null=True, blank=True)
    materia = models.ForeignKey(
        'materia.Materia', on_delete=models.CASCADE, null=True, related_name='cursadas'
    )
    profesor = models.ForeignKey(
        'profesor.Profesor', on_delete=models.CASCADE, null=True, related_name='cursadas'
    )

    def __str__(self):
        return f"{self.id} - {self.materia.nombre if self.materia else 'Sin materia'} - {self.profesor.nombre if self.profesor else 'Sin profesor'} - {self.año} - {self.cuatrimestre}"
    
