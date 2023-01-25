from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    raw_id_fields = ['pedido']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'data_criacao', 'pago']
    list_filter = ['pago', 'data_criacao', 'nome']
    inlines = [ItemPedidoInline]

admin.site.register(Pedido, PedidoAdmin)