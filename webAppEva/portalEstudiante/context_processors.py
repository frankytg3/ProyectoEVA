from webApp.models import  Estudiante

def nombre_estudiante(request):
    if request.user.is_authenticated:
        try:
            estudiante = request.user.estudiante
            nombre_completo = estudiante.nombre_completo()
            return {'nombre_estudiante': nombre_completo}
        except Estudiante.DoesNotExist:
            return {'nombre_estudiante': "USER INVITADO"}
    return {'nombre_estudiante': None}