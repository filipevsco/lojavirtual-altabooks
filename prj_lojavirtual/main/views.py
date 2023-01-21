from django.views.generic.edit import FormView
from main import forms
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto


class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)


def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Produto.objects.filter(categoria=categoria)
    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categorias,
        'lista_produtos': lista_produtos,
    }
    return render(request, 'produto/listar.html', contexto)


def detalhes_produto(request, id, slug_produto):
    produto = get_object_or_404(Produto, id=id, slug=slug_produto, disponivel=True)
    contexto = {
        'produto': produto,
    }
    return render(request, 'produto/detalhes.html', contexto)