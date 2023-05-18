from django.db import models
from django.urls import reverse
import uuid



class Entrega(models.Model):       
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    nome = models.CharField(max_length=255)
    bloco = models.IntegerField()
    andar = models.IntegerField()
    apartamento = models.IntegerField()
    email = models.EmailField()
    data_entrega = models.DateTimeField(auto_now_add=True)
    porteiro = models.ForeignKey('Porteiro', on_delete=models.CASCADE, null=True, blank=True)
    morador = models.ForeignKey('Morador', on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('E', 'Entregue'),
        ('A', 'Aguardando Retirada'),
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')



    def __str__(self):
        return self.nome

class Morador(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    nome = models.CharField(max_length=255)
    bloco = models.IntegerField()
    apartamento = models.IntegerField()
    andar = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Porteiro(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome




