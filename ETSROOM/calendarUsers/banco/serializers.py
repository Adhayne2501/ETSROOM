from rest_framework import serializers
from .models import Evento, Sala, Responsavel, Reserva

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'sala', 'data', 'horario_inicio', 'horario_fim', 'titulo', 'descricao'] 

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade'] 

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['nome', 'email'] 

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['evento', 'participante'] 