from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Emprestimo, Colaborador, Equipamento
from .forms import EmprestimoForm

def deletar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        emprestimo.delete()
        messages.success(request, 'Empréstimo excluído com sucesso!')
        return redirect('listar_emprestimos')
    return render(request, 'emprestimos/deletar_emprestimo.html', {'emprestimo': emprestimo})
    
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()  # Obtém todos os empréstimos
    return render(request, 'emprestimos/listar_emprestimos.html', {'emprestimos': emprestimos})

def atualizar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)

    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo atualizado com sucesso!')
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm(instance=emprestimo)

    return render(request, 'emprestimos/form_emprestimo.html', {'form': form})

def adicionar_emprestimo(request):
    colaboradores = Colaborador.objects.all()  # Obtendo todos os colaboradores
    equipamentos = Equipamento.objects.all()  # Obtendo todos os equipamentos

    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)  # Não salva imediatamente
            emprestimo.colaborador = form.cleaned_data['colaborador']  # Certifique-se de que isso é uma instância
            emprestimo.equipamento = form.cleaned_data['equipamento']  # Certifique-se de que isso é uma instância
            emprestimo.save()  # Salva o objeto de empréstimo
            messages.success(request, 'Empréstimo adicionado com sucesso!')
            return redirect('listar_emprestimos')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

    else:
        form = EmprestimoForm()

    return render(request, 'emprestimos/form_emprestimo.html', {
        'form': form,
        'colaboradores': colaboradores,  # Passando a lista de colaboradores
        'equipamentos': equipamentos,    # Passando a lista de equipamentos
    })
