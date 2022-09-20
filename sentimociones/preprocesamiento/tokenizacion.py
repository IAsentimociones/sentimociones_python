"""
Módulo tokenizacion.py

Implementa estrategias de tokenización con librerías de Natural Language Toolkit
"""
from nltk.tokenize import TreebankWordTokenizer, word_tokenize, regexp_tokenize
import time

import sys
sys.path.append(sys.path[0] + '/..')
from cajaBlanca import logger, auditoria

PROCESO_PRINCIPAL = 'Preprocesamiento'

log = logger.configurar (PROCESO_PRINCIPAL + '.log', __name__)

EXPRESION_REGULAR_ALFABETO = "[A-Za-z][\w']+"
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
    try:
        log.info('Inicia tokenización con expresiones regulares')
        tiempo_inicial = time.time()
        contenido_tokenizado = regexp_tokenize(contenido, EXPRESION_REGULAR_ALFABETO)
        auditoria.registrarPistaProceso([PROCESO_PRINCIPAL + ' Tokenizar con expresiones regulares', tiempo_inicial, ['EXITO']])
        log.info('Finaliza tokenización')
        return contenido_tokenizado
    except:
        log.error("Error al tokenizar con expresiones regulares: ", sys.exc_info()[0])  

