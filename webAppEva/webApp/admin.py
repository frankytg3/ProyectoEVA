from django.contrib import admin
from .models import Curso, Docente, Estudiante, Evaluaciones, Pregunta,Respuesta
from .models import OpcionRespuesta, Calificaciones, MonitoreoExamen  #, salon 
# Register your models here.

class docenteAdmin (admin.ModelAdmin):
    list_display=("user","apellido_paterno","apellido_materno","nombres","telefono","direccion")

class cursoAdmin(admin.ModelAdmin):
    list_display=("nombre","docente")

class estudianteAdmin(admin.ModelAdmin):
    list_display=("user","apellido_paterno","apellido_materno","nombres")

class evaluacionesAdmin (admin.ModelAdmin):
    list_display=("curso","docente","nombre_Evaluacion","numPreguntas","duracion","fecha_creacion","fecha_fin")

class preguntaAdmin(admin.ModelAdmin):
    list_display=("evaluacion","texto","puntos")

class opcionesAdmin(admin.ModelAdmin):
    list_display=("pregunta","opcion","texto_respuesta","es_correcta")

class calificacionesAdmin(admin.ModelAdmin):
    list_display=("estudiante","curso","evaluacion","nota")
class RespuestaAdmin(admin.ModelAdmin):
    list_display=("estudiante","pregunta","opcion_seleccionada","fecha")

class monitoreoAdmin(admin.ModelAdmin):
    list_display=(
        "evaluacion",
        "estudiante",
        "cantErrorFacial",
        "porcenComportamiento",
        "tiempoPromedio",
        "tiempoPorPregunta",
        "tiempoPorPregunta",
        "porcenPlagioTotal",
        "inicio_evaluacion",
        )


# salon--(pendiente)
"""
class SalonAdmin(admin.ModelAdmin):
    list_display = ('cod_seccion', 'modalidad','duracion_clases' , 'hora_inicio', 'hora_fin')
"""

#admin.site.register(salon, SalonAdmin)


admin.site.register(Curso, cursoAdmin)
admin.site.register(Docente, docenteAdmin)
admin.site.register(Estudiante, estudianteAdmin) 
admin.site.register(Evaluaciones,evaluacionesAdmin )
admin.site.register(Pregunta, preguntaAdmin)
admin.site.register(OpcionRespuesta, opcionesAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Calificaciones, calificacionesAdmin)
admin.site.register(MonitoreoExamen, monitoreoAdmin)


