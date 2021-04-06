from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # chave estrangeira p/ classe usuario no App 'usuarios'
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now(), blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos', blank=True)

    def __str__(self):
        return self.nome_receita

# makemigrations - cria novas migracoes
# migrate - sincroniza as migracoes com o BD
