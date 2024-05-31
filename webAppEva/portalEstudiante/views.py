from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from webApp.models import Curso, Evaluaciones, Calificaciones
# Create your views here.

def asignatura(request):
    cursos = Curso.objects.select_related('docente').all()
    context = {
        'cursos': cursos,
    }
    return render(request, "Asignaturas/asignaturas.html",context)


def evaluaciones(request, id):
    curso = get_object_or_404(Curso, id=id)
    evaluaciones = Evaluaciones.objects.filter(curso=curso)
    calificaciones = Calificaciones.objects.filter(estudiante=request.user.estudiante, curso=curso)
    
    context = {
        'curso': curso,
        'evaluaciones': evaluaciones,
        'calificaciones': calificaciones,
    }
    return render(request, 'Asignaturas/evaluaciones.html', context)

def cerrarSecion(request):
    logout(request)
    return redirect('baner')