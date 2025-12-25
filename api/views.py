from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

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
	filter_backends = [filters.SearchFilter]
	search_fields = ['nombre']


class AlumnosViewSet(viewsets.ModelViewSet):
	queryset = Alumnos.objects.all()
	serializer_class = AlumnosSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno']


class SucursalViewSet(viewsets.ModelViewSet):
	queryset = Sucursal.objects.all()
	serializer_class = SucursalSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['nombre', 'ciudad']


class MatriculaViewSet(viewsets.ModelViewSet):
	queryset = Matricula.objects.select_related('curso_codigo', 'alumno_rut', 'sucursal_codigo')
	serializer_class = MatriculaSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['curso_codigo', 'alumno_rut', 'sucursal_codigo', 'fecha']
