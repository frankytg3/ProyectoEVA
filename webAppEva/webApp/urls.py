from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',baner,name='baner'),
    path('home/', home, name='home'),
    path('login/', iniciarsecion, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('registrarDocentes/', registrarDocente, name='registrarDocentes'),
    path('registrarEstudiantes/', registrarEstudiante, name='registrarEstudiantes'),
    path('pruebas/',vistaPrueba, name='vistaprueba')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)