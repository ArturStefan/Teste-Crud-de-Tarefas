from django.db import models
from django.contrib.auth import get_user_model

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    completa = models.BooleanField(default= False)
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    