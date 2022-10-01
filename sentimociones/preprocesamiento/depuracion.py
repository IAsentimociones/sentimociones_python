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
, "e\'", 'pe', 'ale', "ere\'", "atrá\'", 'ey', 'ere\'', 'ey', 'yah', 'uh', 'wh', 'yih', 've\'', 'ra', 'rauw', 'bebã', 'sã', 'letra'
, 'dirã', 'quiã', 'mã', 'dã', 'cã³mo', 'fvck', 'ft', 'jt', 'na', 'cÃ³mo', 'mÃ', 'sÃ', 'cÃ³mo', 'actÃºas', 'tãº', 'actãºas', 'na\''
, 'yeah', 'eh', 'ltima', 'auh', 'auh', 'wuh', 'fa', 'rru', 'tá', 'pi', 'ri', 'farruko', 'yandel', 'reggie', 'miller', 'sech', 'Na'
, 'ovy', 'myke', 'tre', 'parecemo\'', 'ngel', 'to\'', 'jura\'o', 'dólare', 'ovy', 'cru\'', 'somo\'', 'otra\'', 'dólare', 'tapara\''
, 'outro', 'ooh', 'oh', 'pre', 'hey', 'intro', 'verse']

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
        es_traduccion = False
        for palabra in contenido:
            palabra = palabra.lower()
            if (palabra not in palabras_vacias_ingles) and (palabra not in palabras_vacias_espanol) and (palabra not in PALABRAS_VACIAS):
                if palabra == 'Lyrics'.lower():
                    log.debug('Es Lyrics')
                    es_traduccion = True
                else:
                    if palabra == 'Translate'.lower() and es_traduccion:
                        log.debug('Es Translate')
                        break
                    else:
                        es_traduccion = False
                        log.debug(palabra.lower())
                        contenido_depurado.append(palabra.lower())
        
        auditoria.registrarPistaProceso([PROCESO_PRINCIPAL + ' Eliminación de palabras vacías', tiempo_inicial, ['EXITO']])
        log.info('Finlaliza eliminación de palabras vacías')
        return contenido_depurado
    except:
         log.error("Error al eliminar palabras vacías en el proceso de depuración: ", sys.exc_info()[0])



