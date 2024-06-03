from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from webApp.models import Curso, Evaluaciones, Calificaciones, Estudiante,MonitoreoExamen
from datetime import date
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

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
        
        evaluaciones_data = []
        for evaluacion in evaluaciones:
            num_preguntas = evaluacion.pregunta_set.count()
            evaluaciones_data.append({
                'evaluacion': evaluacion,
                'calificacion': calificaciones.filter(evaluacion=evaluacion).first(),
                'num_preguntas': num_preguntas
            })
        
        context = {
            'curso': curso,
            'evaluaciones_data': evaluaciones_data,
            'today': date.today(),
        }
        return render(request, 'Asignaturas/evaluaciones.html', context)
    except ObjectDoesNotExist:
        error = "Error: No se pueden cargar las evaluaciones en este momento. Inténtalo de nuevo más tarde."
        return render(request, 'Asignaturas/evaluaciones.html', {'error': error})

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


@login_required
def detalle_evaluacion(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluaciones, pk=evaluacion_id)
    preguntas = evaluacion.pregunta_set.all()
    total_preguntas = preguntas.count()

    pregunta_idx = int(request.GET.get('pregunta', '0'))

    if pregunta_idx >= total_preguntas:
        return redirect('finalizar_evaluacion', evaluacion_id=evaluacion.id)

    pregunta = preguntas[pregunta_idx]

    if request.method == 'POST':
        seleccion = request.POST.get('opcion')
        calificacion, created = Calificaciones.objects.get_or_create(
            estudiante=request.user.estudiante,
            curso=evaluacion.curso,
            evaluacion=evaluacion,
            defaults={'nota': 0}
        )

        monitoreo_examen, created = MonitoreoExamen.objects.get_or_create(
            evaluacion=evaluacion,
            estudiante=request.user.estudiante,
            defaults={'porcenPlagioTotal': 0, 'cantErrorFacial': 0, 'porcenComportamiento': 0, 'tiempoPromedio': timezone.now(), 'tiempoPorPregunta': timezone.now()}
        )

        if not created:
            # Actualiza la información de monitoreo si es necesario
            monitoreo_examen.tiempoPorPregunta = timezone.now()
            monitoreo_examen.save()

        # Aquí debes guardar la respuesta seleccionada
        # Guardar lógica de respuestas

        return redirect(f'{request.path}?pregunta={pregunta_idx + 1}')

    tiempo_restante = (evaluacion.duracion * 60) - int((timezone.now() - evaluacion.fecha_creacion).total_seconds())

    context = {
        'evaluacion': evaluacion,
        'pregunta': pregunta,
        'pregunta_idx': pregunta_idx + 1,
        'total_preguntas': total_preguntas,
        'opciones': pregunta.opcionrespuesta_set.all(),
        'tiempo_restante': tiempo_restante,
    }
    return render(request, 'Asignaturas/detalle_evaluacion.html', context)

@login_required
def finalizar_evaluacion(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluaciones, id=evaluacion_id)
    curso_id = evaluacion.curso.id
    if request.method == 'POST':
        # Procesa las respuestas y guarda el estado final
        return redirect('evaluaciones', id=curso_id)
    return render(request, 'Asignaturas/finalizar_evaluacion.html', {'evaluacion': evaluacion})

@login_required
def resultado_evaluacion(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluaciones, pk=evaluacion_id)
    calificacion = Calificaciones.objects.filter(
        estudiante=request.user.estudiante,
        evaluacion=evaluacion
    ).first()

    context = {
        'evaluacion': evaluacion,
        'calificacion': calificacion,
    }
    return render(request, 'Asignaturas/resultado_evaluacion.html', context)

