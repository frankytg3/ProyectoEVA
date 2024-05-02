from django.db import models
from .choices import sexos, seccion

# Create your models here.

class Docente(models.Model):
    apellido_paterno=models.CharField(max_length=20, verbose_name='Apeliido Paterno')
    apellido_materno=models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField(verbose_name='fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='F')

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='docente'
        verbose_name_plural='docentes'
        db_table='docente'

    
class Curso(models.Model):
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=1, choices=seccion, default='A')
    docente=models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'
        db_table='cursos'

    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    apellido_paterno=models.CharField(max_length=20, verbose_name='Apeliido Paterno')
    apellido_materno=models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField(verbose_name='fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='F')
    curso=models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    docente=models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='estudiante'
        verbose_name_plural='estudiantes'
        db_table='estudiante'

    