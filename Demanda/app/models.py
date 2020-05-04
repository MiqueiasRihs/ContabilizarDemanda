from django.db import models

# Create your models here.
class Produtos(models.Model):
    TIPO_CHOICES = [
        ("C", "Calçados"),
        ("V", "Vestuario"),
        ("A", "Acessorios"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    marca = models.CharField(max_length=30, null=False, blank=False)
    tamanho = models.CharField(max_length=2, null=False, blank=False)
    quantidade = models.IntegerField(null=False)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, null=False, blank=False)