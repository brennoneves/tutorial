from django.urls import path
from website.views import FuncionariosListView, FuncionariosDeleteView, FuncionariosUpdateView, FuncionariosCreateView

urlpatterns=[
    path(
        'funcionarios/',
        FuncionariosListView.as_view(),
        name='lista_funcionarios'
    ),
    path(
        'funcionario/excluir/<pk>',
        FuncionariosDeleteView.as_view(),
        name='deleta_funcionario'
    ),
    path(
        'funcionario/cadastrar/',
        FuncionariosCreateView.as_view(),
        name='cadastra_funcionario'
    ),
]