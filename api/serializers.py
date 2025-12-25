from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Curso, Alumnos, Sucursal, Matricula


class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class CursoSerializer(ModelSerializer):
    matriculas = SerializerMethodField()

    class Meta:
        model = Curso
        fields = '__all__'

    def get_matriculas(self, obj):
        return MatriculaSerializer(obj.matriculas.all(), many=True).data


class AlumnosSerializer(ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'


class SucursalSerializer(ModelSerializer):
    cantidad_matriculas = SerializerMethodField()

    class Meta:
        model = Sucursal
        fields = '__all__'

    def get_cantidad_matriculas(self, obj):
        return obj.matriculas.count()
