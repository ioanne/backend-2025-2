from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.alumno.models import Alumno


class AlumnoListView(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'alumno_list.html'
    context_object_name = 'alumnos'
