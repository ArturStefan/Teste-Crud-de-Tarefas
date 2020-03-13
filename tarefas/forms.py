from django import forms
from django.forms import ModelForm

from .models import *

class TarefaForm(forms.ModelForm):
    titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Insira aqui uma nova tarefa'}))

    class Meta:
        model = Tarefa
        fields = '__all__'

