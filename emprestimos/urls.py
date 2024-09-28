from django.urls import path
from .views import listar_emprestimos, adicionar_emprestimo, atualizar_emprestimo, deletar_emprestimo

urlpatterns = [
    path('', listar_emprestimos, name='listar_emprestimos'),
    path('adicionar/', adicionar_emprestimo, name='adicionar_emprestimo'),
   path('deletar/<int:pk>/', deletar_emprestimo, name='deletar_emprestimo'),
    path('atualizar/<int:pk>/', atualizar_emprestimo, name='atualizar_emprestimo'),  # A URL deve incluir <int:pk>
]
