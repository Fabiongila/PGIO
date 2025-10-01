from rest_framework import serializers
from .models import Trabalhador, Departamento, RegistroPonto

class TrabalhadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabalhador
        fields = '_all_'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '_all_'

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPonto
        fields = '_all_'