from django.shortcuts import render, redirect
from .models import Departamento, Trabalhador, Usuario
from .forms import DepartamentoForm, TrabalhadorForm, UsuarioForm, ConfiguracaoForm, EditUserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trabalhador, Departamento, RegistroPonto, ConfiguracaoPlataforma
from django.utils import timezone
from django.db.models import Count
from datetime import datetime
from django.contrib.auth.decorators import login_required


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

def novo_trabalhador(request):
    if request.method == 'POST':
        trab_form = TrabalhadorForm(request.POST)
        if trab_form.is_valid():
            trab_form.save()
        return redirect('inicio')
    else:
        trab_form = TrabalhadorForm()
        formulario_trab= {
            'formulario_trab': trab_form
        }
        return render(request, 'account/novo_membro.html', context=formulario_trab)

def lista_membros(request):
    dados ={
        'dados': Trabalhador.objects.all()
    }
    return render(request, 'account/lista_membros.html', context=dados)


def cadastro(request):
    if request.method == 'POST':
        cadastro_form = UsuarioForm(request.POST)
        if cadastro_form.is_valid():
            cadastro_form.save()
        return redirect('inicio')
    else:
        cadastro_form = UsuarioForm()
        formulario_cad= {
            'formulario_cad': cadastro_form
        }
        return render(request, 'account/signup.html', context=formulario_cad)

def configurar_plataforma(request):
    config, created = ConfiguracaoPlataforma.objects.get_or_create(id=1)
    if request.method == 'POST':
        config_form = ConfiguracaoForm(request.POST, request.FILES, instance=config)
        if config_form.is_valid():
            config_form.save()
            return redirect('inicio')
    else:
        config_form = ConfiguracaoForm(instance=config)
    return render(request, 'account/configurar.html', {'form':config_form, 'config': config})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        usuario_form = EditUserForm(request.POST, instance=request.user)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('perfil')
    else:
        usuario_form = EditUserForm(instance=request.user)
    return render(request, 'account/editar_usuario.html', {'form': usuario_form})    



class RelatorioMensalView(APIView):
    def get(self, request):
        mes = request.query_params.get('mes')
        ano = request.query_params.get('ano')

        if not mes or not ano:
            return Response({'erro': 'Forneça mês e ano'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            mes = int(mes)
            ano = int(ano)
        except ValueError:
            return Response({'erro': 'Mês e ano inválidos'}, status=status.HTTP_400_BAD_REQUEST)

        # Filtra presenças do mês
        presencas = RegistroPonto.objects.filter(data_month=mes, data_year=ano)

        # Faltas por trabalhador
        trabalhadores = Trabalhador.objects.all()
        faltas_por_trabalhador = {}
        for trab in trabalhadores:
            total_dias = presencas.filter(trabalhador=trab).count()
            faltas = 30 - total_dias  # suposição de 30 dias
            faltas_por_trabalhador[trab.nome] = faltas

        # Departamentos com mais faltas
        departamentos = Departamento.objects.all()
        faltas_por_departamento = {}
        for dep in departamentos:
            trabs = Trabalhador.objects.filter(departamento=dep)
            total_faltas = 0
            for t in trabs:
                pres = presencas.filter(trabalhador=t).count()
                total_faltas += (30 - pres)
            faltas_por_departamento[dep.nome] = total_faltas

            return Response({
                "faltas_por_trabalhador": faltas_por_trabalhador,
                "faltas_por_departamento": faltas_por_departamento
            })