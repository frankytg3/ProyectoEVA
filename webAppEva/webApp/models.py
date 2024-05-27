from django.db import models
from datetime import timedelta
from .choices import sexos, seccion, modalida, validate_nota, opcionesRpta

# Create your models here.

#tabla Docente -----------------------
class Docente(models.Model):
    apellido_paterno=models.CharField(max_length=20, verbose_name='Apeliido Paterno')
    apellido_materno=models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField(verbose_name='fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='-')
    direccion=models.CharField(max_length=50, verbose_name="dirección",null=True, blank=True)
    telefono=models.CharField(max_length=9,null=True, blank=True)
    

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='docente'
        verbose_name_plural='docentes'
        db_table='docente'


#tabla Curso ------------------------------
class Curso(models.Model):
    nombre=models.CharField(max_length=20)
    
    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'
        db_table='cursos'

    def __str__(self):
        return self.nombre
    

#tabla estudiante-----------------------------
class Estudiante(models.Model):
    apellido_paterno=models.CharField(max_length=20, verbose_name='Apeliido Paterno')
    apellido_materno=models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField(verbose_name='fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='-')
    

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='estudiante'
        verbose_name_plural='estudiantes'
        db_table='estudiante'


# tabla salon ---- (pendiente)----------------

"""
class salon(models.Model):

    cod_seccion = models.CharField(max_length=1, choices=seccion, default='-', verbose_name="Sección")
    modalidad = models.CharField(max_length=2, choices=modalida, default='-')
    duracion_clases = models.IntegerField(blank=True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.hora_inicio and self.duracion_clases:
            self.hora_fin = self.calcular_hora_fin()
        super().save(*args, **kwargs)

    def calcular_hora_fin(self):
        # Calcular la hora de finalización sumando la duración de las clases a la hora de inicio
        hora_fin = self.hora_inicio
        hora_fin = hora_fin.replace(hour=(hora_fin.hour + self.duracion_clases) % 12)
        return hora_fin

    def __str__(self):
        return f"Sección: {self.cod_seccion}, Modalidad: {self.modalidad}, Hora de inicio: {self.hora_inicio.strftime('%I:%M %p')}, Duración: {self.duracion_clases} horas"
    
    
    class Meta:
        verbose_name='salon'
        verbose_name_plural='salones'
        db_table='salones'

"""

#tabla Evaluaciones----------------------    
class Evaluaciones(models.Model):
    
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente=models.ForeignKey(Docente, on_delete=models.CASCADE)
    nombre_Evaluacion=models.CharField(max_length=50, null=True, blank=True)
    numPreguntas=models.IntegerField(validators = [validate_nota])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='evaluacion'
        verbose_name_plural='evaluaciones'
        db_table='evaluaciones'

    def __str__(self):
        return self.nombre_Evaluacion



#tabla preguntas del examnes--------------------------------

class Pregunta(models.Model):
    evaluacion = models.ForeignKey(Evaluaciones, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255) 

    class Meta:
        verbose_name='pregunta'
        verbose_name_plural='preguntas'
        db_table='preguntas'

    def __str__(self):
        return self.texto 

#tabla de opciones de las rpeguntas del examens----------------------
class OpcionRespuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.CharField(max_length=1, choices=opcionesRpta)
    respuesta = models.CharField(max_length=255)
   
#tabla calificaciones------------------------------------------

class Calificaciones(models.Model):
    estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    examen=models.ForeignKey(Evaluaciones,on_delete=models.CASCADE)
    nota=models.FloatField(validators=[validate_nota])
    
#tabla Monitoreo de examen por tiempo

class MonitoreoExamen(models.Model):
    
    evaluacion = models.ForeignKey(Evaluaciones, on_delete=models.CASCADE)
    estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    porcenPlagioTotal=models.FloatField(verbose_name="porcentaje plagio")
    cantErrorFacial=models.IntegerField(verbose_name="errores faciales")
    porcenComportamiento=models.FloatField(verbose_name="comp sospechoso")
    tiempoPromedio=models.TimeField(verbose_name="tiempo examen")
    tiempoPorPregunta=models.TimeField(verbose_name="tiempo pregunta")
   
    
   
    
   


