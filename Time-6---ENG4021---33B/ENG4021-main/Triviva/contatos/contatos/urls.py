from django.urls import path
from . import views

app_name = "contatos"

urlpatterns = [
    path("busca/", views.buscaUmContato, name="busca-contato"),
    path("retorno-busca/", views.respostaBuscaUmContato, name="mostra-contato"),
]