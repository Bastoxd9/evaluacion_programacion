from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CursoViewSet, AlumnosViewSet, SucursalViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'alumnos', AlumnosViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
