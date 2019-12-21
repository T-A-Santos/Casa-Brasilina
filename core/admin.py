from django.contrib import admin
from .models import Cliente, Estoque, Receita, Telefone, Pedido

# Register your models here.


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'telefone', 'get_name')

    def get_name(self, obj):
        return obj.cliente.nome
    get_name.admin_order_field = 'cliente'
    get_name.short_description = 'Nome do cliente'

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtd', 'valor')

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('receita', 'arquivo')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'total', 'observacoes', 'data_entrega', 'entregue')

    def get_name(self, obj):
        return obj.cliente.nome
    get_name.admin_order_field = 'cliente'
    get_name.short_description = 'Nome do cliente'

admin.site.register(Cliente)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Pedido, PedidoAdmin)