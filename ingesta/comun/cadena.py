"""
Módulo cadena.py

Funciones comunes para cadenas de texto o alfanumericos
"""
from re import search
import unicodedata

CARACTERES_ESPECIALES = "!()/[]@:,.-"

def limpiarCaractersEspeciales(cadena):
    """
    Función que elimia caracteres especiales  
    Argumentos:
        cadena: cadena de texto alfanumérico
    Retorna: cadena limpia de caracteres especias
    """
    cadena_sin_caracteres = cadena
    for caracter in CARACTERES_ESPECIALES:
        cadena_sin_caracteres = cadena_sin_caracteres.replace(caracter, "")
    return cadena_sin_caracteres

def limpiarTildes(cadena):
    """
    Función que elimia tildes de una cadena de texto alfanumerico  
    Argumentos:
        cadena: cadena de texto alfanumérico
    Retorna: cadena limpia de tildes
    """
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    cadena_sin_tildes = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', cadena).translate(trans_tab))
    return cadena_sin_tildes

def prepararCadena(cadena):
    """
    Función que prepara una cadena de texto alfanumérico limpiando y estandarizando  
    Argumentos:
        cadena: cadena de texto alfanumérico
    Retorna: cadena preprocesada
    """
    # tranforma cadena minúsculas
    cadena_pre = cadena.casefold();

    # limpia de caracteres especiales
    cadena_pre = limpiarCaractersEspeciales(cadena_pre)

    # limpa de tildes
    cadena_pre = limpiarTildes(cadena_pre)

    return cadena_pre

def contieneCadena(cadena, cadena_completa):
    """
    Función que compara cadena de textos  
    Argumentos:
        cadena: cadena simple
        cadena_completa: cadena completa
    Retorna: True (si la cadena completa contiene la cadena simple)
    """
    # preprocesa cadenas antes de compararlos
    simple = prepararCadena(cadena)
    completa = prepararCadena(cadena_completa)

    print('simple =', simple)
    print('completa =', completa)

    # compara si la cadena completa contiene la cadena simple
    if search(simple, completa):
        return True
    else:
        return False

def cadenaCorta(cadena):
    """
    Función que retorna una cadena corta discriminando caracteres despúes de los espacios  
    Argumentos:
        cadena: cadena con espacios
    Retorna: cadena corta
    """
    cadena_corta = cadena.split(' ')
    return cadena_corta[0]