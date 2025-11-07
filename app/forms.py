from django import forms
from .models import Jogador

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'idade', 'posicao', 'naturalidade', 'foto']
        
        labels = {
            'nome': 'Nome Completo',
            'idade': 'Idade',
            'posicao': 'Posição',
            'naturalidade': 'Naturalidade',
            'foto': 'Foto (Avatar)',
        }