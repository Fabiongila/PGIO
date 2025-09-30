from django.shortcuts import render, redirect
from .models import Departamento, Membros
from .forms import DepartamentoForm, MembrosForm


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
    if request.method == 'POST':
        membro_form = MembrosForm(request.POST)
        if membro_form.is_valid():
            membro_form.save()
        return redirect('inicio')
    else:
        membro_form = MembrosForm()
        formulario_memb= {
            'formulario_memb': membro_form
        }
        return render(request, 'account/novo_membro.html', context=formulario_memb)

def lista_membros(request):
    dados ={
        'dados': Membros.objects.all()
    }
    return render(request, 'account/lista_membros.html', context=dados)