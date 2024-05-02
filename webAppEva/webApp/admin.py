from django.contrib import admin
from .models import Curso, Docente, Estudiante
# Register your models here.

class docenteAdmin (admin.ModelAdmin):
    list_display=("apellido_paterno","apellido_materno","nombres")

class cursoAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","docente")

class estudianteAdmin(admin.ModelAdmin):
    list_display=("apellido_paterno","apellido_materno","nombres","curso","docente")

admin.site.register(Curso, cursoAdmin)
admin.site.register(Docente, docenteAdmin)
admin.site.register(Estudiante, estudianteAdmin) 