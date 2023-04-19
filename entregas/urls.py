from django.contrib import admin
from django.urls import path
from entregas.views import lista_moradores, cadastrar_morador, lista_encomendas,  cadastrar_encomendas, entregues

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', cadastrar_encomendas, name='cadastrar_encomendas'),
    path('lista_moradores/', lista_moradores, name='lista_moradores'),
    path('cadastrar_morador/', cadastrar_morador, name='cadastrar_morador'),
    path('lista_encomendas/', lista_encomendas, name='lista_encomendas'),
    path('entregues/', entregues, name='entregues'),
    ]