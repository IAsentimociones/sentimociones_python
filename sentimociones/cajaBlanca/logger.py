"""
Módulo logger.py

Configura y parametriza el logging para el registro en archivos planos
"""
import logging
import sys

sys.path.append(sys.path[0] + '/..')
FORMATO_LOG = '%(asctime)s - %(levelname)s - %(name)s -  - %(message)s'

PATH_LOGS = sys.path[0] + "/cajaBlanca/logs/"

def configurar(nombreArchivo, nombreClase):
    """
    Función que configura el archivo plano
    Argumentos:
        nombreArchivo: nombre del archivo log
        nombreClase: nombre de la clase
    Retorna: logger configurado
    """
    controlador = logging.FileHandler(PATH_LOGS + nombreArchivo, "w", encoding = "UTF-8")
    formato = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    controlador.setFormatter(formato)
    logger = logging.getLogger(nombreClase)
    logger.addHandler(controlador)
    logger.setLevel(logging.INFO) # utilizar DEBUG para analizar la extracción de letras
    return logger
