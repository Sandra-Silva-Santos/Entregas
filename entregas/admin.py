from django.contrib import admin

# Register your models here.

from .models import Entrega, Morador, Porteiro

admin.site.register(Entrega)
admin.site.register(Morador)
admin.site.register(Porteiro)