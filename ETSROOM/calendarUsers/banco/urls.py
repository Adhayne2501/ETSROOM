from django.urls import path
from .views import EventoListView, EventoDetailView, SalaListView, SalaDetailView, ResponsavelListView, ResponsavelDetailView, ReservaListView, ReservaDetailView

urlpatterns = [
    path('eventos/', EventoListView.as_view(), name='listar_eventos'),
    path('eventos/<int:pk>/', EventoDetailView.as_view(), name='detalhes_evento'),
    path('salas/', SalaListView.as_view(), name='listar_salas'),
    path('salas/<int:pk>/', SalaDetailView.as_view(), name='detalhes_sala'),
    path('responsaveis/', ResponsavelListView.as_view(), name='listar_responsaveis'),
    path('responsaveis/<int:pk>/', ResponsavelDetailView.as_view(), name='detalhes_responsavel'),
    path('reservas/', ReservaListView.as_view(), name='listar_reservas'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='detalhes_reserva'),
]


