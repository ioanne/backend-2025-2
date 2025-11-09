from django.contrib import admin

from apps.cursada.models import Cursada


@admin.register(Cursada)
class CursadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_inicio', 'fecha_fin', 'profesor')
    search_fields = ('id', 'profesor__nombre', 'profesor__apellido')
    list_filter = ('fecha_inicio', 'fecha_fin')
