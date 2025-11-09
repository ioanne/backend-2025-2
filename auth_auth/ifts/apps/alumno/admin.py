from django.contrib import admin

from apps.alumno.models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'id')
    search_fields = ('nombre', 'apellido', 'email', 'id')
    list_filter = ('apellido',)

admin.register(Alumno, AlumnoAdmin)
