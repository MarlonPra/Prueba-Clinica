from django.contrib import admin
from django.urls import path
from clinica import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    # Rutas para Pacientes
    path('paciente/', views.paciente_list, name='paciente_list'),
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    # Rutas para Municipios
    path('municipios/', views.municipio_list, name='municipio_list'),
    path('municipios/crear/', views.municipio_crear, name='municipio_crear'),
    path('municipios/editar/<int:municipio_id>/', views.municipio_editar, name='municipio_editar'),
    path('municipios/eliminar/<int:municipio_id>/', views.municipio_eliminar, name='municipio_eliminar'),
    # Rutas para Diagnosticos
    path('diagnosticos/', views.diagnostico_list, name='diagnostico_list'),
    path('diagnosticos/crear/', views.diagnostico_crear, name='diagnostico_crear'),
    path('diagnosticos/editar/<int:diagnostico_id>/', views.diagnostico_editar, name='diagnostico_editar'),
    path('diagnosticos/eliminar/<int:diagnostico_id>/', views.diagnostico_eliminar, name='diagnostico_eliminar'),
    # Rutas para Historial
    path('historiales/', views.historial_list, name='historial_list'),
    path('historiales/crear/', views.historial_crear, name='historial_crear'),
    path('historiales/editar/<int:historial_id>/', views.historial_editar, name='historial_editar'),
    path('historiales/eliminar/<int:historial_id>/', views.historial_eliminar, name='historial_eliminar')
]
