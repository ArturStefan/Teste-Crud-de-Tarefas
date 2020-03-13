from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="lista_tarefas"),
    path('atualizar_tarefa/<str:pk>/', views.atualizarTarefa, name="atualizar-tarefa"),
    path('deletar_tarefa/<str:pk>/', views.deletarTarefa, name="deletar-tarefa"),
    
]
