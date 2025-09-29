from django.shortcuts import render, redirect
from .models import Departamento
from .forms import DepartamentoForm


def index(request):
    return render(request, "account/index.html")

def main_pag(request):
    return render(request, "account/inicio.html")

def adimistração(request):
    return render(request, 'account/admini.html')

def definições(request):
    return render(request, 'account/definicoes.html')

def novo_departamento(request):
    #instalar a extensão: django-widget-tweaks para estilizar o formulario
    if request.method == 'POST':
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
        return redirect('inicio')
    else:
        departamento_form = DepartamentoForm()
        formulario_dep = {
            'formulario_dep': departamento_form
        }
    return render(request, 'account/novo_departamento.html', context=formulario_dep )

def historico(request):
    return render(request, 'account/historico.html')

def depex(request):
    dados = {
        'dados': Departamento.objects.all()
    }
    return render(request, 'account/depex.html', context=dados)

def novo_membro(request):
    return render(request, 'account/novo_membro.html')

def lista_membros(request):
    return render(request, 'account/lista_membros.html')