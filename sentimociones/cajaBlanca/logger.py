"""
Módulo logger.py

Configura y parametriza el logging para el registro en archivos planos
"""
import logging

FORMATO_LOG = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
FORMATO_FECHA = '%m/%d/%Y %I:%M:%S %p'

def configurar(nombreArchivo, nombreClase):
    """
    Función que configura el archivo plano
    Argumentos:
        nombreArchivo: nombre del archivo log
        nombreClase: nombre de la clase
    Retorna: logger configurado
    """
    logging.basicConfig(filename=nombreArchivo, format=FORMATO_LOG, datefmt=FORMATO_FECHA)
    logger = logging.getLogger(nombreClase)
    logger.setLevel(logging.DEBUG)
       
    return logger