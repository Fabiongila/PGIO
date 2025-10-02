from django.forms import ModelForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from .models import Departamento, Usuario, Trabalhador, ConfiguracaoPlataforma , RegistroPonto, User


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class UsuarioForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        return user

class TrabalhadorForm(ModelForm):
    class Meta:
        model = Trabalhador
        fields = '__all__'

class ConfiguracaoForm(ModelForm):
    class Meta:
        model = ConfiguracaoPlataforma
        fields = ['logotipo']