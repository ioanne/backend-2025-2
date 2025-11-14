from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied

from apps.cursada.models import Cursada
from apps.inscripcion.models import Inscripcion
from apps.profesor.models import Profesor

class CursadaListView(LoginRequiredMixin, ListView):
    model = Cursada
    template_name = 'cursada_list.html'
    context_object_name = 'cursadas'
    # acá puedo agregar ordenamiento/filtros que se procesan en el get_queryset

    # Sobreescribir
    # Extender
    # Como se llama la técnica?
    def get_queryset(self):
        # Acá estoy obteniendo el comportamiento por defectop del método get_queryset
        # Luego lo voy a extender
        queryset = super().get_queryset() # Esta es la clave para entender si vamos a extender
        # Extiendo: porque agrego un filtro
        queryset = queryset.filter(
            profesor__user=self.request.user
        )
        return queryset


class CursadaDetailView(LoginRequiredMixin, DetailView):
    # ¿Para que sirve esto?
    # ¿Quien dice que esto es así?
    # ¿Porque es así?
    model = Cursada
    template_name = 'cursada_detail.html'
    context_object_name = 'cursada'
    pk_url_kwarg = 'id'

    # ¿Que hacemos acá?
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cursada = Cursada.objects.filter(
            id=self.kwargs['id'], profesor__user=self.request.user
        ).first()
        if not cursada:
            # ¿Cuál es el resultado de esta linea?
            raise PermissionDenied("No tienes permiso para ver esta cursada.")

        cursada = Cursada.objects.get(id=self.kwargs['id'])
        
        # ¿Que hacemos acá?
        inscripciones = Inscripcion.objects.filter(cursada=cursada)
        context['cursada'] = {
            "id": cursada.id,
            "nombre": cursada.nombre,
            "profesor": cursada.profesor,
            "alumnos": [
                inscripcion.alumno for inscripcion in inscripciones
            ],
        }

        return context
"""
1. Nos logueamos (/login)
2. Vamos a /cursadas/

Objetivo: ver mis cursadas.


"""


"""
Autorización y autenticación estan bien implementados?
"""