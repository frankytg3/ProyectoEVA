from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("home")

def login(request):
    
    return HttpResponse("login")

def perfilEstudiante(request):
    
    return HttpResponse("perfil Estudiantes")

def asignaturas(request):
    
    return HttpResponse("Asignaturas")

def examenes(request):
    
    return HttpResponse("examenes")

def reporte(request):
    
    return HttpResponse("Reporte")