from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    return render(request, 'tarefas/home.html')

def lista(request):
    
    tarefas = Tarefa.objects.all()
    
    form = TarefaForm()

    if request.method == "POST":
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('lista-tarefas')

    context = {'tarefas': tarefas,'form':form} 
    return render(request, 'tarefas/lista_tarefas.html', context)


def atualizarTarefa(request, pk):
    
    tarefa = Tarefa.objects.get(id=pk)

    form = TarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista-tarefas')
            

    context = {'form':form}
    return render(request, 'tarefas/atualizar_tarefa.html', context)

def deletarTarefa(request, pk):

    item = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('lista-tarefas')

    context ={'item' : item}
    return render(request, 'tarefas/deletar_tarefa.html', context)