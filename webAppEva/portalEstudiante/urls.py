from django.urls import path
from .views import *


urlpatterns = [
    
    path('',baner,name='banerPortal'),
    path('cerrarSecion/',cerrarSecion, name='cerrarsecion'),
]
    