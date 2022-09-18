"""
Módulo tokenizacion.py

Implementa estrategias de tokenización con librerías de Natural Language Toolkit
"""
from nltk.tokenize import TreebankWordTokenizer, word_tokenize, regexp_tokenize

EXPRESION_REGULAR_ALFABETO = "[\w']+"
#https://www.nltk.org/api/nltk.tokenize.regexp.html  OTRAS EXPRESIONES


def tokenizarPorPalabra(contenido):
    """
    Función que tokeniza contenido por palabras
    Argumentos:
        contenido: contenido de texto 
    Retorna: arreglo tokenizado
    """
    return word_tokenize(contenido)

def tokenizarConPuntuacionEspacios(contenido):
    """
    Función que tokeniza contenido por palabras con puntuación y espacios
    Argumentos:
        contenido: contenido de texto 
    Retorna: arreglo tokenizado
    """
    tokenizer = TreebankWordTokenizer()  
    return tokenizer.tokenize(contenido)

def tokenizarConExpresionesRegulares(contenido):
    """
    Función que tokeniza contenido por palabras con expresiones regulares
    Argumentos:
        contenido: contenido de texto 
    Retorna: arreglo tokenizado
    """
    return regexp_tokenize(contenido, EXPRESION_REGULAR_ALFABETO) 

