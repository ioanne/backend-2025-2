from django.contrib import admin

from apps.first_app.models import Ejemplo

# Register your models here.

@admin.register(Ejemplo)
class EjemploAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
