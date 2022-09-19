"""
Módulo depuracion.py

Implementa estrategias de eliminación de palabras: vacías, sin significado, duplicaciones, stop words y números
"""
from nltk.corpus import stopwords

import sys
sys.path.append(sys.path[0] + '/..')

from cajaBlanca import logger
log = logger.configurar ('Preprocesamiento.log', __name__)

PALABRAS_VACIAS = ['tr', 'fact', 'morad', "ale\'", "ilegale\'", "ista\'", 'ja', 'jaja', 'jajaja', 'jajajaja', 'ah', 'lez', 'pa', "pa\'"
, "e\'", 'pe', 'ale', "ere\'", "atrá\'", 'ey', 'ere\'', 'ey', 'yah', 'uh', 'wh', 'yih', 've\'', 'ra', 'rauw']

def eliminarPalabrasVacias(contenido):
    """
    Función que elimina palabras vácias que no tienen significado, duplicaciones y en minúsculas
    Argumentos:
        contenido: contenido de texto 
    Retorna: arreglo depurado
    """
    palabras_vacias_ingles = set(stopwords.words('english'))
    palabras_vacias_espanol = set(stopwords.words('spanish'))

    contenido_depurado = []
    for palabra in contenido:
        palabra = palabra.lower()
        if (palabra not in palabras_vacias_ingles) and (palabra not in palabras_vacias_espanol) and (palabra not in PALABRAS_VACIAS):
            contenido_depurado.append(palabra.upper())

    log.info('TERMINA LA DEPURACION')

    return contenido_depurado



