from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def baner(request):

    return render(request, "portalEstudiante/banerPortal.html")

def cerrarSecion(request):
    logout(request)
    return redirect('baner')