from rest_framework import viewsets

from .models import Curso, Alumnos, Sucursal, Matricula
from .serializers import (
	CursoSerializer,
	AlumnosSerializer,
	SucursalSerializer,
	MatriculaSerializer,
)


class CursoViewSet(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer


class AlumnosViewSet(viewsets.ModelViewSet):
	queryset = Alumnos.objects.all()
	serializer_class = AlumnosSerializer


class SucursalViewSet(viewsets.ModelViewSet):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
	queryset = Matricula.objects.select_related('curso_codigo', 'alumno_rut', 'sucursal_codigo')
	serializer_class = MatriculaSerializer
