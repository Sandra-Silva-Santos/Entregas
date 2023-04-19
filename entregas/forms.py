from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Entrega, Morador
from django.forms.widgets import DateTimeInput



class EntregaForm(forms.ModelForm):
    bloco = forms.IntegerField(required=True, label='Bloco')
    apartamento = forms.IntegerField(required=True, label='Apartamento')
    andar = forms.IntegerField(required=True, label='Andar')
    email = forms.EmailField(required=True, label='Email')  
    entrada = forms.DateTimeField(required=False, label='Data de Entrada', widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    morador = forms.ModelChoiceField(queryset=Morador.objects.all(), empty_label="Selecione um morador", label="Morador")


    class Meta:
        model = Entrega
        fields = [
            'bloco',
            'andar',
            'apartamento',
            'email',
            'morador',
            'entrada',

        ]
        labels = {
            'morador': 'Morador',
            'nome': 'Nome',
            'bloco': 'Bloco',
            'andar': 'Andar',
            'apartamento': 'Apartamento',
            'email': 'Email',
            'entrada': 'Data de Entrada',

        }


class MoradorForm(forms.ModelForm):
    nome = forms.CharField(required=True, label='Nome')
    bloco = forms.IntegerField(required=True, label='Bloco')
    apartamento = forms.IntegerField(required=True, label='Apartamento')
    andar = forms.IntegerField(required=True, label='Andar')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = Morador
        fields = [
            'nome',
            'bloco',
            'andar',
            'apartamento',
            'email',
        ]
        labels = {
            'nome': 'Nome',
            'bloco': 'Bloco',
            'andar': 'Andar',
            'apartamento': 'Apartamento',
            'email': 'Email',
        }

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        bloco = cleaned_data.get('bloco')
        apartamento = cleaned_data.get('apartamento')
        andar = cleaned_data.get('andar')
        email = cleaned_data.get('email')

        if Morador.objects.filter(Q(nome=nome) & Q(bloco=bloco) & Q(apartamento=apartamento) & Q(andar=andar) & Q(email=email)).exists():
            raise ValidationError('Morador já cadastrado')    

