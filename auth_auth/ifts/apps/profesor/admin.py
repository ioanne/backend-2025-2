from django.contrib import admin

from apps.profesor.models import Profesor


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'id')
    search_fields = ('nombre', 'apellido', 'email', 'id')
    list_filter = ('apellido',)