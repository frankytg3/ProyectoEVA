from django.urls import path
from .views import *


urlpatterns = [
    
    path('',asignatura,name='asignatura'),
    path('cerrarSecion/',cerrarSecion, name='cerrarsecion'),
    path('curso/<int:id>/', evaluaciones, name='evaluaciones'),
    path('evaluacion/<int:evaluacion_id>/', detalle_evaluacion, name='detalle_evaluacion'),
    path('evaluacion/<int:evaluacion_id>/finalizar/', finalizar_evaluacion, name='finalizar_evaluacion'),
    path('evaluacion/<int:evaluacion_id>/resultado/', resultado_evaluacion, name='resultado_evaluacion'),
    path('retroalimentacion/<int:evaluacion_id>/', retroalimentacion, name='retroalimentacion'),
    
]

