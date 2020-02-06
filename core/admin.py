from django.contrib import admin
from .models import Cliente, Estoque, Pedido


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome','bairro','CEP','rua','numero','cpf','cnpj','telefone','descricao')
    search_field = ('id','nome','cpf')

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','nome','qtd','valor','data_entrada','data_vencimento')
    search_field = ('id','nome')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','total','pedido','data_entrega')
    search_field = ('id','cliente')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Pedido, PedidoAdmin)
