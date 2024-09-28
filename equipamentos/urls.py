
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),  # Página inicial vai para a lista de equipamentos
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),  # Adicionar equipamento
    path('atualizar/<int:pk>/', views.atualizar_equipamento, name='atualizar_equipamento'),  # Atualizar equipamento
    path('deletar/<int:pk>/', views.deletar_equipamento, name='deletar_equipamento'),  # Deletar equipamento
]