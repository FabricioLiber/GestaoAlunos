from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=10, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_alunos', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
