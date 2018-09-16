from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm


# Create your views here.
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'list.html', {'alunos': alunos})


def cadastrar_aluno(request):
    form = AlunoForm(request.POST or None, request.FILES or None, None)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'cadastrar.html', {'form' : form})

def atualizar_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'cadastrar.html', {'form' : form})

def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)

    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, 'deletar.html', {'aluno' : aluno})

def ver_perfil(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'perfil.html', {'aluno' : aluno})
