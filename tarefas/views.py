from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):

    tarefas = Tarefa.objects.all()
    
    form = TarefaForm()

    if request.method == "POST":
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('/')

    context = {'tarefas': tarefas,'form':form} 

    return render(request, 'tarefas/lista.html', context)