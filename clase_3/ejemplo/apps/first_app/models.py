from django.db import models

# Create your models here.
class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    ada = models.foreignKey('self', on_delete=models.CASCADE, null=True, blank=True)