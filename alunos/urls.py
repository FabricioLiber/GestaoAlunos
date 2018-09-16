from django.urls import path
from .views import listar_alunos
from .views import cadastrar_aluno
from .views import atualizar_aluno
from .views import deletar_aluno
from .views import ver_perfil


urlpatterns = [
    path('', listar_alunos, name = "listar_alunos"),
    path('new/', cadastrar_aluno, name = "cadastrar_aluno"),
    path('update/<int:id>/', atualizar_aluno, name = "atualizar_aluno"),
    path('delete/<int:id>/', deletar_aluno, name = "deletar_aluno"),
    path('perfil/<int:id>/', ver_perfil, name = "ver_perfil")
]
