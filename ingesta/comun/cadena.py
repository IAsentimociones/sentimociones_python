"""
Módulo cadena.py

Funciones comunes para cadenas de texto o alfanumericos
"""
from re import search

def contieneCadena(cadena, cadena_completa):
    """
    Función que compara cadena de textos  
    Argumentos:
        cadena: cadena simple
        cadena_completa: cadena completa
    Retorna: True (si la cadena completa contiene la cadena simple)
    """
    # transforma para discriminar minúsculas y mayúsculas
    simple = cadena.casefold()
    completa = cadena_completa.casefold()

    # compara si la cadena completa contiene la cadena simple
    if search(simple, completa):
        return True
    else:
        return False