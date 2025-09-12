from django.db import models


class Institucional(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    historia = models.TextField()

    def __str__(self):
        return self.nombre