from django.urls import path

from apps.alumno.views import AlumnoListView


urlpatterns = [
    path('', AlumnoListView.as_view(), name='alumno_list'),
]