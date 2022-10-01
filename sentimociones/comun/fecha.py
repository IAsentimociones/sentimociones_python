"""
Módulo fecha.py

Funciones comunes para fechas
"""
from datetime import datetime

FORMATO_FECHA_TIEMPO = "%d/%m/%Y %H:%M:%S"

def obtenerFechaTiempoActual():
    """
    Función que obtiene la fecha tiempo actual  
    Retorna: fecha tiempo actual en formato día mes año hora:minuto:segundo
    """
    fecha_tiempo_actual = datetime.now()
    fecha_tiempo_formateado = fecha_tiempo_actual.strftime(FORMATO_FECHA_TIEMPO)
    return fecha_tiempo_formateado