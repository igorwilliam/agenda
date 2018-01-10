from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from.forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefa
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def novaCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:listaCategorias')
            #return HttpResponse('Categoria adicionada com sucesso !!!')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form': form})

@login_required
def listaCategorias(request):
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'tarefas/lista_categorias.html', {'categorias': categorias})

@login_required
def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(user=request.user, data=request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('core')
            #return HttpResponse('Tarefa adicionada com sucesso !!!')
        else:
            print(form.errors)
    else:
        form = TarefaForm(user=request.user)
    return render(request, 'tarefas/nova_Tarefa.html', {'form': form})

@login_required
def deleteTarefa(request, id):
    tarefa = Tarefa.objects.get(id=id, user=request.user).delete() #ou pk esse eh um alias
    return redirect('core')

@login_required
def editarTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    if request.method == 'POST':
        form = TarefaForm(user=request.user, data=request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core')
    else:
        form = TarefaForm(user=request.user, instance=tarefa)
    return render(request,'tarefas/nova_tarefa.html', {'form': form})

@login_required
def deleteCategoria(request, id):
    categoria = Categoria.objects.get(id=id, user=request.user).delete()
    return redirect('tarefas:listaCategorias')

@login_required
def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id, user=request.user)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save();
            return redirect('tarefas:listaCategorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render (request, 'tarefas/nova_categoria.html', {'form': form})

@login_required
def search(request):
    q = request.GET.get('search')
    if q is not None:
        result = Tarefa.objects.search(q, request.user)
    return render(request, 'tarefas\pagina_resultado.html', {'result':result})

@login_required
def detalhesTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    return render(request, 'tarefas/detalhes_tarefa.html', {'tarefa': tarefa})
