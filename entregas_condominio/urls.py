"""entregas_condominio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from entregas.views import lista_moradores, cadastrar_morador, lista_encomendas,  cadastrar_encomendas, aguardando_retirada, entregues

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', cadastrar_encomendas, name='cadastrar_encomendas'),
    path('lista_moradores/', lista_moradores, name='lista_moradores'),
    path('cadastrar_morador/', cadastrar_morador, name='cadastrar_morador'),
    path('lista_encomendas/', lista_encomendas, name='lista_encomendas'),
    path('aguardando_retirada/', aguardando_retirada, name='aguardando_retirada'),
    path('entregues/', entregues, name='entregues'),
    ]