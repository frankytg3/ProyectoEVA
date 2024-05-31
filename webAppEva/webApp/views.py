from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from webApp.forms import FormDocentes, FormEstudiate,FormPrueba, FormCurso
from webApp.models import Docente, Estudiante
from django.contrib import messages
# Create your views here.

def registrarDocente(request):
    if request.method == "POST":
        formDocente = FormDocentes(request.POST)
        formRegister = UserCreationForm(request.POST)
        if formDocente.is_valid() and formRegister.is_valid():
            try:
                user = formRegister.save(commit=False)
                user.email = formDocente.cleaned_data['correo']
                user.save()
                
                # Crear docente asociado al usuario
                Docente.objects.create(
                    user=user,
                    apellido_paterno=formDocente.cleaned_data['apellido_Paterno'],
                    apellido_materno=formDocente.cleaned_data['apellido_Materno'],
                    nombres=formDocente.cleaned_data['nombres'],
                    fecha_nacimiento=formDocente.cleaned_data['fecha_Nacimiento'],
                    sexo=formDocente.cleaned_data['sexo'],
                    direccion=formDocente.cleaned_data['direccion'],
                    telefono=formDocente.cleaned_data['telefono']
                )
                
                messages.success(request, 'Docente registrado exitosamente. Por favor inicia sesión.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Error: El nombre de usuario ya está en uso.')
        else:
            messages.error(request, 'Existen errores en los Datos del Usuario')
    else:
        formDocente = FormDocentes()
        formRegister = UserCreationForm()
    
    return render(request, "registration/registrarDocentes.html", {
        'formUser': formRegister,
        'formDocente': formDocente,
        'pagina': 'registrarDocente',
    })


def registrarEstudiante(request):
    if request.method == "POST":
        formEstudiante = FormEstudiate(request.POST)
        formRegister = UserCreationForm(request.POST)
        if formEstudiante.is_valid() and formRegister.is_valid():
            try:
                correo = formEstudiante.cleaned_data['correo']
                user = formRegister.save(commit=False)  # Guardar usuario
                user.email = correo  # Establecer el correo electrónico del usuario
                user.save()
                # Crear estudiante asociado al usuario
                Estudiante.objects.create(
                    user=user,
                    apellido_paterno=formEstudiante.cleaned_data['apellido_Paterno'],
                    apellido_materno=formEstudiante.cleaned_data['apellido_Materno'],
                    nombres=formEstudiante.cleaned_data['nombres'],
                    fecha_nacimiento=formEstudiante.cleaned_data['fecha_Nacimiento'],
                    sexo=formEstudiante.cleaned_data['sexo'],
                )
                messages.success(request, 'Usuario registrado exitosamente. Por favor inicia sesión.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'Error: El nombre de usuario ya está en uso.')
    else:
        formEstudiante = FormEstudiate()
        formRegister = UserCreationForm()
    
    return render(request, "registration/registrarEstudiantes.html", {
        'formUser': formRegister,
        'formEstudiante': formEstudiante,
        'pagina': 'registrarEstudiante',
    })


def iniciarsecion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('asignatura')
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



