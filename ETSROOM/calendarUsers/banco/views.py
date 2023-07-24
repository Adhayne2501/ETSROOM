from rest_framework import generics
from .models import Evento, Sala, Responsavel, Reserva
from .serializers import EventoSerializer, SalaSerializer, ResponsavelSerializer, ReservaSerializer

class EventoListView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class SalaListView(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class SalaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class ResponsavelListView(generics.ListCreateAPIView):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class ResponsavelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class ReservaListView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer