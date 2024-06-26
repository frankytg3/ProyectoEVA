from django.core.exceptions import ValidationError

sexos=(
    ('F','femenino'),
    ('M','masculino')
)
seccion=(
    ('A','seccion A'),
    ('B','Seccion B'),
    ('C','seccion c'),
    ('D','seccion D')
)

modalida=(
    ('PR','PRESENCIAL'),
    ('SM','SEMIPRESENCIAL'),
    ('VT','VIRTUAL')
    
)
persona=(
    ('estudiante','ESTUDIANTE'),
    ('profesor','PROFESOR')
    
)
opcionesRpta=(
    ('A','opcion A'),
    ('B','opcion B'),
    ('C','opcion C'),
    ('D','opcion D')
)




def validate_nota(value):
    if value < 0 or value > 20:
        raise ValidationError('solo entre 0 y 20.')