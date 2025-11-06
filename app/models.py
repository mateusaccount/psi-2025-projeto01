from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='images/posts/')
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo