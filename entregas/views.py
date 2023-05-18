from .forms import EntregaForm
from .models import Entrega , Morador
from django.shortcuts import render, redirect
from .forms import MoradorForm
import uuid



def entregues(request):
    entregas = Entrega.objects.all()
    return render(request, 'entregues.html', {'entregues': entregas})
    

def aguardando_retirada(request):
    pendentes = Entrega.objects.all()
    return render(request, 'aguardando_retirada.html', {'pendentes': pendentes})


def lista_encomendas(request):
    entregas = Entrega.objects.all()
    return render(request, 'lista_encomendas.html', {'encomendas': entregas})
    

def lista_moradores(request):
    moradores = Morador.objects.all()
    return render(request, 'lista_moradores.html', {'moradores': moradores})    


def cadastrar_morador(request):
    form = MoradorForm(request.POST)
    if form.is_valid():
        morador = form.save(commit=False)
        morador.id = str(uuid.uuid4())
        morador.save()
        return redirect('/lista_moradores/')
    else:
        form = MoradorForm()
    return render(request, 'cadastrar_morador.html', {'form': form})
    


def cadastrar_encomendas(request):
    form = EntregaForm(request.POST)
    if form.is_valid():
        entrega = form.save(commit=False)
        entrega.id = str(uuid.uuid4())
        entrega.save()
        return redirect('/lista_encomendas/')
    else:
        form = EntregaForm()
    return render(request, 'cadastrar_encomendas.html', {'form': form})





