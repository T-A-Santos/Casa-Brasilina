from django.contrib import admin
from .models import Cliente, Estoque, Pedido


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','bairro','CEP','rua','numero','cpf','cnpj')

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('nome','qtd','valor','data_entrada','data_vencimento')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente','total','pedido','data_entrega')

admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Telefone)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Pedido, PedidoAdmin)
