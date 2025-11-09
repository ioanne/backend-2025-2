from django.contrib import admin

from apps.inscripcion.models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'cursada', 'fecha_inscripcion')
    search_fields = ('alumno__nombre', 'alumno__apellido', 'cursada__nombre')
    list_filter = ('fecha_inscripcion',)
