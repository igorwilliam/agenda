from django.urls import path

from . import views

app_name = 'tarefas'
urlpatterns = [
    path('lista-categorias/',views.listaCategorias, name="listaCategorias"),

    path('nova-categoria/',views.novaCategoria, name="novaCategoria"),
    path('nova-tarefa/',views.novaTarefa, name="novaTarefa"),

    path('delete-tarefa/(?P<id>[0-9]+)/',views.deleteTarefa, name="deleteTarefa"),
    path('editar-tarefa/(?P<id>[0-9]+)/',views.editarTarefa, name="editarTarefa"),

    path('editar-categoria/(?P<id>[0-9]+)/', views.editarCategoria, name="editarCategoria"),
    path('delete-categoria/(?P<id>[0-9]+)/', views.deleteCategoria, name="deleteCategoria"),

    path('detalhes_tarefa/(?P<id>[0-9]+)/', views.detalhesTarefa, name="detalhesTarefa"),

    path('buscar/', views.search, name="search"),
]
