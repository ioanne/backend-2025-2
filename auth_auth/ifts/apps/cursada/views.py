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

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            profesor__user=self.request.user
        )
        return queryset

class CursadaDetailView(LoginRequiredMixin, DetailView):
    model = Cursada
    template_name = 'cursada_detail.html'
    context_object_name = 'cursada'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cursada = Cursada.objects.filter(id=self.kwargs['id'], profesor__user=self.request.user).first()
        if not cursada:
            raise PermissionDenied("No tienes permiso para ver esta cursada.")

        cursada = Cursada.objects.get(id=self.kwargs['id'])
        
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