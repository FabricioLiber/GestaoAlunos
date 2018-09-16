from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'data_nasc', 'sexo', 'foto']
