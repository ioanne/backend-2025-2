from django.db import models


class Category(models.Model): # tabla
    name = models.CharField(max_length=100) # campo
    description = models.TextField() # campo

    def __str__(self):
        return self.name


class CategoryItem(models.Model): # tabla
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # campo
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE) # campo

    def __str__(self):
        return f"{self.category.name} - {self.item.name}"