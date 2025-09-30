from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nome_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.TextField(max_length=12)

    def __str__(self):
        return self.user.username

class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=25)
    gestor = models.CharField(max_length=50)
    descrição = models.TextField(max_length=5000)


class Membros(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    profissão = models.CharField(max_length=25)
    número = models.IntegerField()
    email = models.EmailField(max_length=25)