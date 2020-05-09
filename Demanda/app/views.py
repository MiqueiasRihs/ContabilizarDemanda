from django.shortcuts import render, redirect
from .forms import ProdutosForm
from .entidades.produtos import Produtos
from .services import produto_service


def delete_produto(request, id):
    if(request.GET.get('delete_produto')):
        produto_id = produto_service.listar_produtos_id(id)
        produto_service.remover_produto(produto_id)
        return redirect('produtos_demanda')

### Metodo para renderizar na tela ###
def produtos_demanda(request):
    if request.method == "POST":
        form_produtos = ProdutosForm(request.POST)
        if form_produtos.is_valid():
            nome = form_produtos.cleaned_data["nome"]
            marca = form_produtos.cleaned_data["marca"]
            tamanho = form_produtos.cleaned_data["tamanho"]
            quantidade = form_produtos.cleaned_data["quantidade"]
            tipo = form_produtos.cleaned_data["tipo"]

            produtos_novos = Produtos(nome=nome, marca=marca, tamanho=tamanho, quantidade=quantidade, tipo=tipo)
            produto_service.cadastrar_produto(produtos_novos)

            return redirect('produtos_demanda')
    else:
        form_produtos = ProdutosForm()

    form_produtos = ProdutosForm()

    produto = produto_service.listar_produtos()

    return render(request, 'produtos_demanda.html', {"form_produtos": form_produtos, "produto": produto})


