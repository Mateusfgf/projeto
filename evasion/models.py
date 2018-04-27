from django.db import models
from django.utils import timezone



class Aluno(models.Model):

    nome = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    idade = models.IntegerField(default=0)
    curso = models.CharField(max_length=200)
    renda = models.CharField(max_length=200)
    residencia = models.TextField()
    quantos_km = models.IntegerField(default=0) 
    renda_familiar = models.IntegerField(default=0) 
    ja_possui_graducao = models.BooleanField(default=False)
    ja_possui_tecnico = models.BooleanField(default=False)
    curso_em_andamento = models.BooleanField(default=False)
    data_resposta = models.DateTimeField(
            default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Graduacao_fazendo_tecnico(models.Model):

    id_aluno = models.ForeignKey(Aluno)
    inicio_curso = models.IntegerField(default=0)
    fim_curso = models.IntegerField(default=0)
    data_resposta = models.DateTimeField(
            default=timezone.now)

class Tecnico_fazendo_graducacao(models.Model):
    id_aluno = models.ForeignKey(Aluno)
    inicio_curso = models.IntegerField(default=0)
    fim_curso = models.IntegerField(default=0)
    data_resposta = models.DateTimeField(
            default=timezone.now)
