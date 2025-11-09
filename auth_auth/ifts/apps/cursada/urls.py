from django.urls import path

from apps.cursada.views import CursadaListView, CursadaDetailView

urlpatterns = [
    path('', CursadaListView.as_view(), name='cursada_list'),
    path('<int:id>/', CursadaDetailView.as_view(), name='cursada_detail'),
]