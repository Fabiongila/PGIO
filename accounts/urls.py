from django.urls import path, include
from . import views
#from .views import TrabalhadorListCreateView, TrabalhadorDetailView
#from .views import DepartamentoListCreateView, DepartamentoDetailView
from .views import RelatorioMensalView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.main_pag, name="inicio"),
    path('inicio/', views.edit_profile, name="editar_usuario"),
    path('configurar/', views.configurar_plataforma, name='configurar'),
    #path('cadastro/', views.novo_trabalhador, name="login"),
    #path('login/', views.login, name="login"),
    path('admini/', views.adimistração, name="admini"),
    path('definicoes/', views.definições, name='definicoes'),
    path('novo_departamento/', views.novo_departamento, name='novo_departamento'),
    path('historico/', views.historico, name='historico'),
    path('depex/', views.depex, name='depex'),
    path('novo_trabalhador/', views.novo_trabalhador, name='novo_membro'),
    path('lista_membros/', views.lista_membros, name='lista_membros'),

    #path('trabalhadores/', TrabalhadorListCreateView.as_view(), name='listar_criar_trabalhadores'),
    #path('trabalhadores/<int:pk>/', TrabalhadorDetailView.as_view(), name='detalhe_trabalhador'),

    #path('departamentos/', DepartamentoListCreateView.as_view(), name='listar_criar_departamentos'),
    #path('departamentos/<int:pk>/', DepartamentoDetailView.as_view(), name='detalhe_departamento'),

    path('relatorios/mensal/', RelatorioMensalView.as_view(), name='relatorio_mensal'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)


