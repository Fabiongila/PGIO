from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=25, null=True)
    nome_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.TextField(max_length=12)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=25)
    gestor = models.CharField(max_length=50)
    descrição = models.TextField(max_length=5000)

    def __str__(self):
        return self.nome_departamento
    

class Trabalhador(models.Model):
    nome = models.CharField(max_length=50)
    profissão = models.CharField(max_length=25)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, related_name='trabalhadores' , null=True, blank=True)
    número = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)
    data_contratacao = models.DateField()

    def _str_(self):
        return self.nome


class ConfiguracaoPlataforma(models.Model):
    nome_empresa = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='logos/', null=True)

    def __str_(self):
        return self.nome_empresa


class RegistroPonto(models.Model):
    
    STATUS_CHOICES = [
        ('presente', 'Presente'),
        ('falta', 'Falta'),
        ('justificada', 'Justificada'),
    ]

    trabalhador = models.ForeignKey(Trabalhador, on_delete=models.CASCADE)
    data = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_saida = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='presente')

    def str(self):
        return f"{self.trabalhador.nome} - {self.data} ({self.status})"