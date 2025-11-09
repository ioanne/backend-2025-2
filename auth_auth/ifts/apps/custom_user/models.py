from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
#pedro.picapiedra
#holamundo666

#juan.perez
#holamundo666
