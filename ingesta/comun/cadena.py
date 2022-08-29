"""
Módulo cadena.py

Funciones comunes para cadenas de texto o alfanumericos
"""
from re import search

CARACTERES_ESPECIALES = "!()/[]@"

def limpiarCadena(cadena):
    """
    Función que limia caracteres especiales  
    Argumentos:
        cadena: cadena de texto alfanumérico
    Retorna: cadena limpia de caracteres especias
    """
    cadena_limpia = cadena
    for caracter in CARACTERES_ESPECIALES:
        cadena_limpia = cadena_limpia.replace(caracter, "")
    return cadena_limpia

def contieneCadena(cadena, cadena_completa):
    """
    Función que compara cadena de textos  
    Argumentos:
        cadena: cadena simple
        cadena_completa: cadena completa
    Retorna: True (si la cadena completa contiene la cadena simple)
    """
    # preprocesa cadenas antes de compararlos
    simple = limpiarCadena(cadena.casefold())
    completa = limpiarCadena(cadena_completa.casefold())

    # compara si la cadena completa contiene la cadena simple
    if search(simple, completa):
        return True
    else:
        return False