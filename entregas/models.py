from django.db import models
from django.urls import reverse
import uuid

class Entrega(models.Model):
    ENTREGUE = 'E'
    PENDENTE = 'P'
    STATUS_CHOICES = [
        (ENTREGUE, 'Entregue'),
        (PENDENTE, 'Pendente'),
    ]
    
    
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    nome = models.CharField(max_length=255)
    bloco = models.IntegerField()
    andar = models.IntegerField()
    apartamento = models.IntegerField()
    email = models.EmailField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    data_entrega = models.DateTimeField(auto_now_add=True)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('entrega-detail', kwargs={'pk': self.pk})



class Morador(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    nome = models.CharField(max_length=255)
    bloco = models.IntegerField()
    apartamento = models.IntegerField()
    andar = models.IntegerField()
    email = models.EmailField()



    def __str__(self):
        return self.nome