from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.data} {self.horario_inicio} - {self.horario_fim}"
    
class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Reserva(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participante.nome} - {self.evento.titulo}"
