from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from webApp.models import Curso, Evaluaciones, Calificaciones, Estudiante
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def asignatura(request):
    cursos = Curso.objects.select_related('docente').all()
    context = {
        'cursos': cursos,
    }
    return render(request, "Asignaturas/asignaturas.html",context)

def evaluaciones(request, id):
    try:
        curso = get_object_or_404(Curso, id=id)
        evaluaciones = Evaluaciones.objects.filter(curso=curso)
        calificaciones = Calificaciones.objects.filter(estudiante=request.user.estudiante, curso=curso)
        
        context = {
            'curso': curso,
            'evaluaciones': evaluaciones,
            'calificaciones': calificaciones,
            'today': date.today(),
        }
        return render(request, 'Asignaturas/evaluaciones.html', context)
    except ObjectDoesNotExist:
        error = "Error: No se pueden cargar las evaluaciones en este momento. Inténtalo de nuevo más tarde."
        return render(request, 'Asignaturas/evaluaciones.html', {'error': error})

def detalle_evaluacion(request, id):
    evaluacion = get_object_or_404(Evaluaciones, id=id)
    return render(request, 'Asignaturas/detalle_evaluacion.html', {'evaluacion': evaluacion})

def cerrarSecion(request):
    logout(request)
    return redirect('baner')

def nombre_estudiante(request):
    if request.user.is_authenticated:
        try:
            estudiante = Estudiante.objects.get(user=request.user)
            return {'nombre_estudiante': estudiante.nombre}
        except Estudiante.DoesNotExist:
            return {'nombre_estudiante': "Nombre Predeterminado"}
    return {'nombre_estudiante': None}