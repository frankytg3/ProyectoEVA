from django.urls import path
from .views import *


urlpatterns = [
    
    path('',baner,name='baner'),
    path('home/', home, name='home'),
    path('login/', iniciarsecion, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('registrarDocentes/', registrarDocente, name='registrarDocentes'),
    path('registrarEstudiantes/', registrarEstudiante, name='registrarEstudiantes'),
    path('pruebas/',vistaPrueba, name='vistaprueba')
    
]
    