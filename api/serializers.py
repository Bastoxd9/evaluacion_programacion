from rest_framework import serializers
from .models import Curso, Alumnos, Sucursal, Matricula


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
