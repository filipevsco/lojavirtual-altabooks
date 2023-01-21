from decimal import Decimal
from django.conf import settings
from main.models import Produto

class Carrinho:
    def __init__(self, request):
        self.__sessao = request.session
        carrinho = self.__sessao.get(settings.ID_CARRINHO)
        if not carrinho:
            carrinho = self.__sessao[settings.ID_CARRINHO] = {}
        self.__carrinho = carrinho
    
    def adicionar(self, produto, quantidade=1, atualizar_quantidade=False):
        id_produto = str(produto.id)
        if id_produto not in self.__carrinho:
        pass