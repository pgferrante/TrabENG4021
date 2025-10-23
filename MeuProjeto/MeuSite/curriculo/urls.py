from django.urls import path
from . import views

app_name = 'curriculo'

urlpatterns = [
    # essa rota pode ser acessada em /curriculo/spiff/
    # ou seja, /curriculo/ + spiff/
    # o link para essa rota pode ser criado usando o nome 'curriculo_spiff'
    # Exemplo: {% url 'curriculo:curriculo_spiff' %}
    path('index/', views.index, name='index'),
    # essa rota pode ser acessada em /curriculo/spiff/v2/
    path('meu/curriculo/', views.meu-curriculo, name='meu-curriculo'),
]