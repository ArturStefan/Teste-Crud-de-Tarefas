from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('lista_tarefas', views.lista, name="lista-tarefas"),
    path('atualizar_tarefa/<str:pk>/', views.atualizarTarefa, name="atualizar-tarefa"),
    path('deletar_tarefa/<str:pk>/', views.deletarTarefa, name="deletar-tarefa"),
    path('registro/', include('django.contrib.auth.urls'))
]
