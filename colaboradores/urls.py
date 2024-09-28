from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_colaboradores, name='listar_colaboradores'),
    path('adicionar/', views.adicionar_colaborador, name='adicionar_colaborador'),
    path('atualizar/<int:pk>/', views.atualizar_colaborador, name='atualizar_colaborador'),
    path('deletar/<int:pk>/', views.deletar_colaborador, name='deletar_colaborador'),
]
