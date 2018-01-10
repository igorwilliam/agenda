from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from hello.tarefas.models import Tarefa

@login_required
def home(request):
    tarefas = Tarefa.objects.filter(user=request.user, status='') #select * from tarefa; ORM object relationship Manager
    return render(request, 'core/index.html', {'tarefas': tarefas})
    #haahahah
