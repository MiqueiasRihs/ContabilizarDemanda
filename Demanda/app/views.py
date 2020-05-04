from django.shortcuts import render
from .forms import ProdutosForm

# Create your views here.
def produtos_demanda(request):
    form_produtos = ProdutosForm()
    return render(request, 'produtos_demanda.html', {"form_produtos": form_produtos})