from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from webApp.models import Curso, Evaluaciones, Calificaciones, Estudiante,MonitoreoExamen, OpcionRespuesta, Respuesta
from datetime import date , timedelta
import pytz

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

@login_required
def evaluaciones(request, id):
    try:
        curso = get_object_or_404(Curso, id=id)
        evaluaciones = Evaluaciones.objects.filter(curso=curso)
        calificaciones = Calificaciones.objects.filter(estudiante=request.user.estudiante, curso=curso)
        monitoreo_examen = MonitoreoExamen.objects.filter(evaluacion__in=evaluaciones, estudiante=request.user.estudiante).first()
        
        evaluaciones_data = []
        today = date.today()

        if monitoreo_examen:
            monitoreo=True

        for evaluacion in evaluaciones:
            num_preguntas = evaluacion.pregunta_set.count()
            calificacion = calificaciones.filter(evaluacion=evaluacion).first()
            estado = 'Sin evaluar'

            if calificacion:
                if calificacion.nota > 0 or monitoreo:
                    estado = 'Realizada'
            elif evaluacion.fecha_fin and evaluacion.fecha_fin.date() < today:
                estado = 'Caducada'
            else:
                estado = 'Disponible'

            evaluaciones_data.append({
                'evaluacion': evaluacion,
                'calificacion': calificacion,
                'num_preguntas': num_preguntas,
                'estado': estado,
            })
        
        context = {
            'curso': curso,
            'evaluaciones_data': evaluaciones_data,
            'today': today,
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
        # Calcular la nota final antes de redirigir
        calificacion = Calificaciones.objects.get(
            estudiante=request.user.estudiante,
            curso=evaluacion.curso,
            evaluacion=evaluacion,
        )
        calificacion.nota = sum(
            [r.pregunta.puntos for r in Respuesta.objects.filter(estudiante=request.user, pregunta__evaluacion=evaluacion, opcion_seleccionada__es_correcta=True)]
        )
        calificacion.save()
        return redirect('finalizar_evaluacion', evaluacion_id=evaluacion.id)

    pregunta = preguntas[pregunta_idx]

    monitoreo_examen = MonitoreoExamen.objects.filter(evaluacion=evaluacion, estudiante=request.user.estudiante).first()

    if not monitoreo_examen:
        # Si no existe un registro en MonitoreoExamen, crea uno
        monitoreo_examen = MonitoreoExamen.objects.create(
            evaluacion=evaluacion,
            estudiante=request.user.estudiante,
            porcenPlagioTotal=0,
            cantErrorFacial=0,
            porcenComportamiento=0,
            tiempoPromedio=timezone.now(),
            tiempoPorPregunta=timezone.now(),
            inicio_evaluacion=timezone.now()
        )
    

    if request.method == 'POST':
        seleccion_id = request.POST.get('opcion')
        if seleccion_id:
            seleccion = OpcionRespuesta.objects.get(id=seleccion_id)
            Respuesta.objects.create(
                estudiante=request.user,
                pregunta=pregunta,
                opcion_seleccionada=seleccion
            )

        calificacion, created = Calificaciones.objects.get_or_create(
            estudiante=request.user.estudiante,
            curso=evaluacion.curso,
            evaluacion=evaluacion,
            defaults={'nota': 0}
        )

        # Actualiza el tiempo de la pregunta
        monitoreo_examen.tiempoPorPregunta = timezone.now()
        monitoreo_examen.save()

        return redirect(f'{request.path}?pregunta={pregunta_idx + 1}')
    
    # Calcula el tiempo restante basado en el inicio de la evaluación y la zona horaria local
    zona_horaria = pytz.timezone('America/Lima')  # Cambia a la zona horaria que necesites
    tiempo_inicio = monitoreo_examen.inicio_evaluacion.astimezone(zona_horaria)
    tiempo_actual = timezone.now().astimezone(zona_horaria)
    tiempo_pasado = tiempo_actual - tiempo_inicio

    # Convertir la duración de la evaluación a timedelta
    duracion_evaluacion = timedelta(minutes=evaluacion.duracion)

    # Calcular el tiempo restante restando el tiempo pasado de la duración total
    tiempo_restante_timedelta = duracion_evaluacion - tiempo_pasado  
    tiempo_restante = int(tiempo_restante_timedelta.total_seconds())

    minutos_restantes = tiempo_restante // 60
    segundos_restantes = tiempo_restante % 60

    context = {
        'evaluacion': evaluacion,
        'pregunta': pregunta,
        'pregunta_idx': pregunta_idx + 1,
        'total_preguntas': total_preguntas,
        'opciones': pregunta.opcionrespuesta_set.all(),
        'minutos_restantes': minutos_restantes,
        'segundos_restantes': segundos_restantes,
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

@login_required
def retroalimentacion(request, evaluacion_id):
    evaluacion =  get_object_or_404(Evaluaciones, pk=evaluacion_id)
    curso = evaluacion.curso 
    # Puedes pasar datos adicionales a la plantilla si es necesario
    context = {'evaluacion': evaluacion,
               'curso': curso,
               }
    
    return render(request, 'Asignaturas/retroalimentacion.html', context)


