from webApp.models import  Estudiante

def nombre_estudiante(request):
    if request.user.is_authenticated:
        try:
            estudiante = request.user.estudiante
            nombre_completo = estudiante.nombre_completo()
            foto_url = estudiante.foto.url if estudiante.foto else None
            return {'nombre_estudiante': nombre_completo, 'foto_estudiante': foto_url}
        except Estudiante.DoesNotExist:
            return {'nombre_estudiante': "USER INVITADO", 'foto_estudiante': None}
    return {'nombre_estudiante': None, 'foto_estudiante': None}
