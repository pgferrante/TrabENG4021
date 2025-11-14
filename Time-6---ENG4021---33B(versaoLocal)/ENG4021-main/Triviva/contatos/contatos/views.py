from django.shortcuts import render
from .models import Pessoa

def buscaUmContato(request):
    # Mostra o formulário de busca
    return render(request, "contatos/buscaUmContato.html")

def respostaBuscaUmContato(request):
    # Lê o que o usuário digitou e filtra no banco
    termo = request.GET.get("nome", "")
    pessoas = Pessoa.objects.all().filter(nome__icontains=termo)
    contexto = {"pessoas": pessoas}
    return render(request, "contatos/listaContatos.html", contexto)