from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    carrera = models.ForeignKey(
        'carrera.Carrera', on_delete=models.CASCADE, null=True, related_name='materias'
    )

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.codigo}) - {self.carrera.nombre if self.carrera else 'Sin carrera'}"

# Ejemplo de querys
# from apps.carrera.models import Carrera
# Materia.objects.create(nombre="Backend", codigo="BK-DS", carrera_id=1)
# Materia.objects.create(nombre="Tecnicas de Programacion", codigo="TP-DS", carrera=Carrera.objects.get(id=1))

# Materia.objects.last()
# Materia.objects.first()

# Materia.objects.all()
# Materia.objects.filter(nombre__icontains="tecnicas")

