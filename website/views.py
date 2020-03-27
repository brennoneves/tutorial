from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from helloworld.models import Funcionarios
from website.forms import InsereFuncionarioForm

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class FuncionariosListView(ListView):
    template_name = "website/lista.html"
    model = Funcionarios
    context_object_name = "funcionarios"

class FuncionariosUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionarios
    fields = '__all__'
    context_object_name = 'funcionarios'

    def get_object(self, queryset=None):
        funcionario=None

        id=self.kwargs.get(self.pk_url_kwarg)
        slug=self.kwargs.get(self.slug_url_kwarg)

        if id is not None:

            funcionario = Funcionarios.objects.filter(id=id).first()

        elif slug is not None:

            campo_slug=self.get_slug_field()
            funcionario= Funcionarios.objects.filter(**{campo_slug: slug}).first()

        return funcionario

class FuncionariosDeleteView(DeleteView):
    template_name = 'website/exclui.html'
    model=Funcionarios
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )


class FuncionariosCreateView(CreateView):
    template_name = 'webiste/cria.html'
    model = Funcionarios
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy(
        'website:lista_funcionarios'
    )




