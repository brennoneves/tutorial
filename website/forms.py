from django import forms
from helloworld.models import Funcionarios

"""
class InsereFuncionarioForm(forms.Form):

    nome= forms.CharField(
        required=True,
        max_length=255
    )

    sobrenome= forms.CharField(
        required=True,
        max_length=255
    )

    cpf= forms.CharField(
        required=True,
        max_length=14
    )

    tempo_de_servico=forms.IntegerField(
        required=True
    )

    remuneracao = forms.DecimalField()

"""
# Outro modo de fazer mais simples
class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        model= Funcionarios

        fields =[
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao'
        ]

        exclude = [
            'tempo_de_servico'
        ]
