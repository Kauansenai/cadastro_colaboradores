from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Colaborador
from .forms import ColaboradorForm

def home(request):
    return render(request, 'colaboradores/home.html')

def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores/listar_colaboradores.html', {'colaboradores': colaboradores})

def adicionar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores/form_colaborador.html', {'form': form})

def atualizar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'colaboradores/form_colaborador.html', {'form': form})

def deletar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('listar_colaboradores')
    return render(request, 'colaboradores/confirmar_delete.html', {'colaborador': colaborador})
