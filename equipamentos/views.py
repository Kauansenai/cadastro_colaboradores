from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Equipamento
from .forms import EquipamentoForm

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/listar_equipamentos.html', {'equipamentos': equipamentos})

def adicionar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento adicionado com sucesso!')
            return redirect('listar_equipamentos')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            print(form.errors)
    else:
        form = EquipamentoForm()

    return render(request, 'equipamentos/form_equipamento.html', {'form': form})

def atualizar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)

    return render(request, 'equipamentos/form_equipamento.html', {'form': form})

def deletar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento deletado com sucesso!')
        return redirect('listar_equipamentos')

    return render(request, 'equipamentos/confirmar_delete.html', {'equipamento': equipamento})  # Corrigido aqui
