from django.contrib import admin
from .models import Contato


class formContato(admin.ModelAdmin):
    list_display = ['nome', 'email','mensagem']

admin.site.register(Contato, formContato)
