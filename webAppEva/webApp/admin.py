from django.contrib import admin
from .models import Curso, Docente, Estudiante, Evaluaciones, Pregunta
from .models import OpcionRespuesta, Calificaciones, MonitoreoExamen  #, salon 
# Register your models here.

class docenteAdmin (admin.ModelAdmin):
    list_display=("apellido_paterno","apellido_materno","nombres","telefono","direccion")

class cursoAdmin(admin.ModelAdmin):
    list_display=("nombre","docente")

class estudianteAdmin(admin.ModelAdmin):
    list_display=("user","apellido_paterno","apellido_materno","nombres")

class evaluacionesAdmin (admin.ModelAdmin):
    list_display=("curso","docente","nombre_Evaluacion","numPreguntas","fecha_creacion")

class preguntaAdmin(admin.ModelAdmin):
    list_display=("evaluacion","texto")

class opcionesAdmin(admin.ModelAdmin):
    list_display=("pregunta","opcion","respuesta")

class calificacionesAdmin(admin.ModelAdmin):
    list_display=("estudiante","curso","examen","nota")

class monitoreoAdmin(admin.ModelAdmin):
    list_display=("evaluacion","estudiante","cantErrorFacial","porcenComportamiento","tiempoPromedio","tiempoPorPregunta","tiempoPorPregunta","porcenPlagioTotal")

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
admin.site.register(Calificaciones, calificacionesAdmin)
admin.site.register(MonitoreoExamen, monitoreoAdmin)

