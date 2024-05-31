# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_by_evaluacion(calificaciones, evaluacion):
    return calificaciones.filter(evaluacion=evaluacion).first()