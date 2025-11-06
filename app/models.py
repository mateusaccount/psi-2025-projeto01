from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='images/posts/')
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    posicao = models.CharField(max_length=50)
    naturalidade = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='images/jogadores/')

    def __str__(self):
        return self.nome