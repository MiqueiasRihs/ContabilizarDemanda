from ..models import Produtos

def cadastrar_produto(produtos):
    Produtos.objects.create(nome=produtos.nome, marca=produtos.marca, tamanho=produtos.tamanho, quantidade=produtos.quantidade, tipo=produtos.tipo)

def listar_produtos():
    return Produtos.objects.all()

def listar_produtos_id(id):
    return Produtos.objects.get(id=id)

def remover_produto(produto_id):
    produto_id.delete()