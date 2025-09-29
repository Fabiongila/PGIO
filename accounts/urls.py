from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.main_pag, name="inicio"),
    path('admini/', views.adimistração, name="admini"),
    path('definicoes/', views.definições, name='definicoes'),
    path('novo_departamento/', views.novo_departamento, name='novo_departamento'),
    path('historico/', views.historico, name='historico'),
    path('depex/', views.depex, name='depex'),
    path('novo_membro/', views.novo_membro, name='novo_membro'),
    path('lista_membros/', views.lista_membros, name='lista_membros'),

]
