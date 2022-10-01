"""
Módulo tokenizacion.py

Implementa estrategias de tokenización con librerías de Natural Language Toolkit
"""
from nltk.tokenize import TreebankWordTokenizer, word_tokenize, regexp_tokenize
import re 
from collections import Counter
import time
import sys


sys.path.append(sys.path[0] + '/..')
from cajaBlanca import logger, auditoria

PROCESO_PRINCIPAL = 'Preprocesamiento'

log = logger.configurar (PROCESO_PRINCIPAL + '.log', __name__)

EXPRESION_REGULAR_ALFABETO = "[A-Za-z][\w']+"
EXPRESION_REGULAR_ALFANUMERICO = '[^a-z0-9#]'


def tokenizarPorPalabra(contenido):
    """
    Función que tokeniza contenido por palabras
    Argumentos:
        contenido: contenido de textoo 
    Retorna: arreglo tokenizado
    """
    return word_tokenize(contenido)

def tokenizarConPuntuacionEspacios(contenido):
    """
    Función que tokeniza contenido por palabras con puntuación y espacios
    Argumentos:
        contenido: contenido de textoo 
    Retorna: arreglo tokenizado
    """
    tokenizer = TreebankWordTokenizer()  
    return tokenizer.tokenize(contenido)

def tokenizarConExpresionesRegulares(contenido):
    """
    Función que tokeniza contenido por palabras con expresiones regulares
    Argumentos:
        contenido: contenido de textoo 
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

def tokenizar_oracion(token, n):
    """
    Función recursiva que tokeniza una oración
    Argumentos:
        contenido: contenido de textoo 
    Retorna: arreglo tokenizado
    """ 
    output = []
    for i in range(n-1, len(token)): 
        tokenizar_oracion = ' '.join(token[i-n+1:i+1])
        output.append(tokenizar_oracion) 
    return output

def crear_caracteristica(texto, nrange=(1, 1)):
    caracteristicas_textoo = [] 
    texto = texto.lower() 
    texto_alfanumerico = re.sub(EXPRESION_REGULAR_ALFANUMERICO, ' ', texto)
    for n in range(nrange[0], nrange[1]+1): 
        caracteristicas_textoo += tokenizar_oracion(texto_alfanumerico.split(), n)    
    texto_punc = re.sub('[a-z0-9]', ' ', texto)
    caracteristicas_textoo += tokenizar_oracion(texto_punc.split(), 1)
    return Counter(caracteristicas_textoo)
