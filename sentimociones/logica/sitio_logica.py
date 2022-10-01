"""
Módulo sitio.py

Implementación de lógica de sitios web
"""
from datetime import date
import sys
sys.path.append(sys.path[0] + '/..')
from bdd import mongoDB_cliente
from cajaBlanca import logger

log = logger.configurar ('GestionSitio.log', __name__)

def insertarSitio(url, lista_canciones ):
    """
    Función que inserta una coleccion del sitio web
    Argumentos:
        url: dirección de la página o sitio web 
        lista_canciones: lista de canciones obtenida en ese sitio web
    Retorna: identificador principial del sitio web registrado en BDD
    """
    try:
        log.info('Registra en base de datos sitio web de las canciones extraidas')
        fecha_actual = date.today()
        coleccionSitio = {"url": url, "fecha_extraccion": fecha_actual.strftime("%d/%m/%Y"), "lista_canciones": lista_canciones}
        sitio_id = mongoDB_cliente.insertarDocumento("SITIOS", coleccionSitio)
        
        return sitio_id
    except:
        log.error("Error al registrar sitio en base de datos: ", sys.exc_info()[0])

