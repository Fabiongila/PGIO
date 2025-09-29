from django.forms import ModelForm
from .models import Departamento

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'