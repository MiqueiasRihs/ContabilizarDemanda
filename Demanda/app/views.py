from django.shortcuts import render

# Create your views here.
def produtos_demanda(request):
    return render(request, 'produtos_demanda.html')