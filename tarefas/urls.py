from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="lista"),
    path('atualizar_tarefa/<str:pk>/', views.atualizarTarefa, name="atualizar-tarefa"),
    
]
