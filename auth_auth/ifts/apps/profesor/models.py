from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user = models.OneToOneField('custom_user.CustomUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"