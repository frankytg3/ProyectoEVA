
from django import forms
from webApp.choices import sexos, persona
from django.core.exceptions import ValidationError
from .models import Evaluaciones, Estudiante

def dominio_continental_validator(value):
    if not value.endswith('@continental.edu.pe'):
        raise ValidationError('El correo debe ser @continental.edu.pe')

def no_numeros_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El campo no debe contener números')
    
def no_letras_validator(value):
    if any(char.isalpha() for char in value):
        raise ValidationError('El campo no debe contener letras')  
    
class FormDocentes(forms.Form):
    correo = forms.EmailField(label="Correo electrónico",validators=[dominio_continental_validator])
    apellido_Paterno = forms.CharField(max_length=100,validators=[no_numeros_validator])
    apellido_Materno = forms.CharField(max_length=100,validators=[no_numeros_validator])
    nombres = forms.CharField(max_length=100,validators=[no_numeros_validator])
    fecha_Nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(max_length=50, label="Dirección", required=False)
    telefono = forms.CharField(max_length=9, required=False,validators=[no_letras_validator])
    sexo = forms.ChoiceField(choices=sexos, initial='-')

class FormEstudiate(forms.Form):
    correo = forms.EmailField(label="Correo electrónico",validators=[dominio_continental_validator])
    apellido_Paterno=forms.CharField(max_length=20,validators=[no_numeros_validator])
    apellido_Materno=forms.CharField(max_length=20,validators=[no_numeros_validator])   
    nombres=forms.CharField(max_length=20,validators=[no_numeros_validator])
    fecha_Nacimiento=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sexo = forms.ChoiceField(choices=sexos, initial='-')
    foto = forms.ImageField(required=True)

    class Meta:
        model = Estudiante
        fields = ['correo', 'apellido_Paterno', 'apellido_Materno', 'nombres', 'fecha_Nacimiento', 'sexo', 'foto']
    
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            if not foto.name.endswith('.png'):
                raise ValidationError("Solo se permiten archivos PNG.")
            if foto.content_type != 'image/png':
                raise ValidationError("Solo se permiten archivos PNG.")
        return foto

    
class FormOpcion(forms.Form):
    Persona = forms.ChoiceField(choices=persona)


class FormPrueba(forms.Form):
    gmail = forms.EmailField(validators=[dominio_continental_validator])
    nombre = forms.CharField(max_length=20, validators=[no_numeros_validator])
    
class FormCurso(forms.ModelForm):
    
     class Meta:
        model=Evaluaciones
        fields = ['curso','docente','nombre_Evaluacion','numPreguntas']