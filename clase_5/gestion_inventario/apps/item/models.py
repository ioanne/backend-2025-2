from django.db import models


class Item(models.Model): # tabla
    name = models.CharField(max_length=100) # Campo
    description = models.TextField() # Campo

    def __str__(self):
        return self.name
