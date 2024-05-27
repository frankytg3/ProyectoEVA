from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from webApp.forms import FormDocentes, FormEstudiate,FormPrueba, FormCurso
from webApp.models import Docente, Estudiante
# Create your views here.

def registrarDocente(request):
    
    formdocente = FormDocentes()
    formRegister = UserCreationForm() 
        
    if request.method == "GET":
        print("mostrando formulario")  
        return render(request, "registration/registrarDocentes.html", {
            'formUser':formRegister,
            'formDocente':formdocente,
            'pagina': 'registrarDocente'
        })  
        
    elif request.method == "POST":
        
        print("enviar datos...")
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        
        if pass1 == pass2:
            print("contraseña valida ")
            formdocente = FormDocentes(request.POST)
            formRegister = UserCreationForm(request.POST)
            if formdocente.is_valid():
                try:
                    nomUser=request.POST['username']
                    correo=request.POST['correo']
                    paterno=request.POST['apellido_Paterno']
                    materno=request.POST['apellido_Materno']
                    nombre=request.POST['nombres']
                    nacimiento=request.POST['fecha_Nacimiento']
                    sex=request.POST['sexo']
                    direcc=request.POST['direccion']
                    celular=request.POST['telefono']
        
                    print("guardando datos usuario y docente")
                    user = User.objects.create_user(username=nomUser,email=correo, password=pass1)
                    user.save()
                    
                    profesor= Docente.objects.create(
                        apellido_paterno=paterno,
                        apellido_materno=materno,
                        nombres=nombre,
                        fecha_nacimiento=nacimiento,
                        sexo=sex,
                        direccion=direcc,
                        telefono=celular
                    )
                    profesor.save()
                    
                    return redirect('login')
                except IntegrityError:
                    return render(request, "registration/registrarDocentes.html", {
                    'formUser':formRegister,
                    'formDocente':formdocente,
                    'pagina': 'registrarDocente'
                    })   
            else:
                print("hay errores en los datos")
                
                return render(request, "registration/registrarDocentes.html", {
                    'formUser':formRegister,
                    'formDocente':formdocente,
                    'errorp':"Existen errores en los Datos del Usuario",
                    'pagina': 'registrarDocente'
                })
        else:              
            return render(request, "registration/registrarDocentes.html", {
                'formUser':formRegister,
                'formDocente':formdocente,
                'errorp':"Contraseñas Diferentes ",
                'pagina': 'registrarDocente'
            })

from django.contrib.auth import login  # Importa la función login de django.contrib.auth

def registrarEstudiante(request):
    
    formEstudiante = FormEstudiate()
    formRegister = UserCreationForm() 
        
    if request.method == "GET":
        print("mostrando formulario")  
        return render(request, "registration/registrarEstudiantes.html", {
            'formUser':formRegister,
            'formEstudiante':formEstudiante,
            'pagina': 'registrarEstudiante',
        })  
        
    elif request.method == "POST":
        
        print("enviar datos...")
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        
        if pass1 == pass2:
            print("contraseña valida ")
            formEstudiante = FormEstudiate(request.POST)
            formRegister = UserCreationForm(request.POST)
            if formEstudiante.is_valid():
                try:
                    nomUser=request.POST['username']
                    correo=request.POST['correo']
                    paterno=request.POST['apellido_Paterno']
                    materno=request.POST['apellido_Materno']
                    nombre=request.POST['nombres']
                    nacimiento=request.POST['fecha_Nacimiento']
                    sex=request.POST['sexo']
                    
        
                    print("guardando datos usuario y Estudiante")
                    user = User.objects.create_user(username=nomUser,email=correo, password=pass1)
                    user.save()
                    
                    estudiante= Estudiante.objects.create(
                        apellido_paterno=paterno,
                        apellido_materno=materno,
                        nombres=nombre,
                        fecha_nacimiento=nacimiento,
                        sexo=sex,
                        
                    )
                    estudiante.save()
                    
                    return redirect('login')  
                
                except IntegrityError:
                    return render(request, "registration/registrarEstudiantes.html", {
                    'formUser':formRegister,
                    'formEstudiante':formEstudiante,
                    'pagina': 'registrarEstudiante',
                    })   
            else:
                print("hay errores en los datos")
                
                return render(request, "registration/registrarEstudiantes.html", {
                    'formUser':formRegister,
                    'formEstudiante':formEstudiante,
                    'errorp':"Existen errores en los Datos del Usuario",
                    'pagina': 'registrarEstudiante',
                })
        else:              
            return render(request, "registration/registrarEstudiantes.html", {
                'formUser':formRegister,
                'formEstudiante':formEstudiante,
                'errorp':"Contraseñas Diferentes ",
                'pagina': 'registrarEstudiante'
            })

def iniciarsecion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {
                'pagina': 'inicio',
                'formLogin': form,
            })
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {
            'pagina': 'inicio',
            'formLogin': form
        })

        
         
def cerrarSecion(request):
    logout(request)
    return redirect('baner')
    

def vistaPrueba(request):
    if request.method == "POST":
        form = FormCurso(request.POST)
        if form.is_valid():
            # Aquí puedes hacer algo con los datos válidos, como guardarlos en la base de datos
            return render(request, "webApp/pruebas.html", {'formprueba': form})
    else:
        form = FormCurso()
    
    # Si el formulario no es válido o si es una solicitud GET, renderiza el formulario con los posibles errores
    return render(request, "webApp/pruebas.html", {'formprueba': form})


def home(request):

    return render(request, "webApp/home.html")

def baner(request):

    return render(request, "webApp/baner.html", {'pagina': 'inicio'})

def registrar(request):
    return render(request, 'registration/registrar.html', {'pagina': 'registrar'})



