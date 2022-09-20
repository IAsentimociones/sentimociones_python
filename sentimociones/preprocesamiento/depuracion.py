"""
Módulo depuracion.py

Implementa estrategias de eliminación de palabras: vacías, sin significado, duplicaciones, stop words y números
"""
from nltk.corpus import stopwords
import time

import sys
sys.path.append(sys.path[0] + '/..')
from cajaBlanca import logger, auditoria

PROCESO_PRINCIPAL = 'Preprocesamiento'

log = logger.configurar (PROCESO_PRINCIPAL + '.log', __name__)

PALABRAS_VACIAS = ['tr', 'fact', 'morad', "ale\'", "ilegale\'", "ista\'", 'ja', 'jaja', 'jajaja', 'jajajaja', 'ah', 'lez', 'pa', "pa\'"
, "e\'", 'pe', 'ale', "ere\'", "atrá\'", 'ey', 'ere\'', 'ey', 'yah', 'uh', 'wh', 'yih', 've\'', 'ra', 'rauw']

def eliminarPalabrasVacias(contenido):
    """
    Función que elimina palabras vácias que no tienen significado, duplicaciones y en minúsculas
    Argumentos:
        contenido: contenido de texto 
    Retorna: arreglo depurado
    """
    try:
        log.info('Inicia eliminación de palabras vacías y stop words')
        tiempo_inicial = time.time()
        palabras_vacias_ingles = set(stopwords.words('english'))
        palabras_vacias_espanol = set(stopwords.words('spanish'))

        contenido_depurado = []
        for palabra in contenido:
            palabra = palabra.lower()
            if (palabra not in palabras_vacias_ingles) and (palabra not in palabras_vacias_espanol) and (palabra not in PALABRAS_VACIAS):
                contenido_depurado.append(palabra.upper())
        
        auditoria.registrarPistaProceso([PROCESO_PRINCIPAL + ' Eliminación de palabras vacías', tiempo_inicial, ['EXITO']])
        log.info('Finlaliza eliminación de palabras vacías')
        return contenido_depurado
    except:
         log.error("Error al eliminar palabras vacías en el proceso de depuración: ", sys.exc_info()[0])



