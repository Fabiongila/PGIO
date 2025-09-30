from django.forms import ModelForm
from .models import Departamento, Usuario, Membros

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields = '__all__'

class MembrosForm(ModelForm):
    class Meta:
        model = Membros
        fields = '__all__'