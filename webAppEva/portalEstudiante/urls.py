from django.urls import path
from .views import *


urlpatterns = [
    
    path('',asignatura,name='asignatura'),
    path('cerrarSecion/',cerrarSecion, name='cerrarsecion'),
    path('curso/<int:id>/', evaluaciones, name='evaluaciones'),
    path('evaluacion/<int:id>/', detalle_evaluacion, name='detalle_evaluacion'),
]
    