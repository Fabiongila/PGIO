from django.forms import ModelForm
from .models import Departamento, Usuario, Trabalhador, ConfiguracaoPlataforma , RegistroPonto, User


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields = '__all__'

class TrabalhadorForm(ModelForm):
    class Meta:
        model = Trabalhador
        fields = '__all__'

class ConfiguracaoForm(ModelForm):
    class Meta:
        model = ConfiguracaoPlataforma
        fields = ['nome_empresa', 'logotipo']