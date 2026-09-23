from django.shortcuts import render, redirect
from .forms import PacienteForm, MunicipioForm, DiagnosticoForm, HistorialForm
from .models import Paciente, Municipio, Diagnostico, Historial
from django.db.models import Q
from django.contrib import messages


def inicio(request):
    return render(request, 'clinica/inicio.html')
#-------------PACIENTES----------------
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/paciente_list.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente creado exitosamente.')
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'clinica/crear_paciente.html', {'form': form})

def editar_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado exitosamente.')
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'clinica/editar_paciente.html', {'form': form, 'paciente': paciente})

def eliminar_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado exitosamente.')
        return redirect('paciente_list')
    return render(request, 'clinica/confirmar_eliminar_paciente.html', {'paciente': paciente})

#-------------MUNICIPIOS----------------
def municipio_list(request):
    municipios = Municipio.objects.all()
    return render(request, 'clinica/municipio_list.html', {'municipios': municipios})

def municipio_crear(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Municipio creado exitosamente.')
            return redirect('municipio_list')
    else:
        form = MunicipioForm()
    return render(request, 'clinica/municipio_crear.html', {'form': form})

def municipio_editar(request, municipio_id):
    municipio = Municipio.objects.get(id=municipio_id)
    if request.method == 'POST':
        form = MunicipioForm(request.POST, instance=municipio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Municipio actualizado exitosamente.')
            return redirect('municipio_list')
    else:
        form = MunicipioForm(instance=municipio)
    return render(request, 'clinica/municipio_editar.html', {'form': form, 'municipio': municipio})

def municipio_eliminar(request, municipio_id):
    municipio = Municipio.objects.get(id=municipio_id)
    if request.method == 'POST':
        municipio.delete()
        messages.success(request, 'Municipio eliminado exitosamente.')
        return redirect('municipio_list')
    return render(request, 'clinica/confirmar_eliminar_municipio.html', {'municipio': municipio})

#-------------DIAGNOSTICOS----------------
def diagnostico_list(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'clinica/diagnostico_list.html', {'diagnosticos': diagnosticos})

def diagnostico_crear(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diagnóstico creado exitosamente.')
            return redirect('diagnostico_list')
    else:
        form = DiagnosticoForm()
    return render(request, 'clinica/diagnostico_crear.html', {'form': form})

def diagnostico_editar(request, diagnostico_id):
    diagnostico = Diagnostico.objects.get(id=diagnostico_id)
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diagnóstico actualizado exitosamente.')
            return redirect('diagnostico_list')
    else:
        form = DiagnosticoForm(instance=diagnostico)
    return render(request, 'clinica/diagnostico_editar.html', {'form': form})

def diagnostico_eliminar(request, diagnostico_id):
    diagnostico = Diagnostico.objects.get(id=diagnostico_id)
    if request.method == 'POST':
        diagnostico.delete()
        messages.success(request, 'Diagnóstico eliminado exitosamente.')
        return redirect('diagnostico_list')
    return render(request, 'clinica/confirmar_eliminar_diagnostico.html', {'diagnostico': diagnostico})

#-------------HISTORIAL----------------
def historial_list(request):
    historiales = Historial.objects.all()
    if request.method == 'GET':
        busqueda = request.GET.get('q', '')
        if busqueda:
            historiales = historiales.filter(Q(paciente__nombre__icontains=busqueda) | Q(diagnostico__nombre__icontains=busqueda) | Q(diagnostico__codigo__icontains=busqueda))
    return render(request, 'clinica/historial_list.html', {'historiales': historiales, 'busqueda': busqueda})

def historial_crear(request):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial creado exitosamente.')
            return redirect('historial_list')
    else:
        form = HistorialForm()
    return render(request, 'clinica/historial_crear.html', {'form': form})

def historial_editar(request, historial_id):
    historial = Historial.objects.get(id=historial_id)
    if request.method == 'POST':
        form = HistorialForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial actualizado exitosamente.')
            return redirect('historial_list')
    else:
        form = HistorialForm(instance=historial)
    return render(request, 'clinica/historial_editar.html', {'form': form})

def historial_eliminar(request, historial_id):
    historial = Historial.objects.get(id=historial_id)
    if request.method == 'POST':
        historial.delete()
        messages.success(request, 'Historial eliminado exitosamente.')
        return redirect('historial_list')
    return render(request, 'clinica/confirmar_eliminar_historial.html', {'historial': historial})
