from ..models import Produtos

def cadastrar_produto(produto):
    Produtos.objects.create(nome=Produtos.nome, marca=Produtos.marca, tamanho=Produtos.tamanho, quantidade=Produtos.quantidade, tipo=Produtos.tipo)