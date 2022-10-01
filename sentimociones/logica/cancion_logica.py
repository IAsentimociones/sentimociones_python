"""
Módulo cancion.py

Implementación de lógica de negocio para canciones
"""
import sys
sys.path.append(sys.path[0] + '/..')
from bdd import mongoDB_cliente
from cajaBlanca import logger

log = logger.configurar ('GestionCanciones.log', __name__)


ESTADO_SIN_LETRA = "SIN LETRA"
ESTADO_CON_LETRA = "CON LETRA"
ESTADO_NO_ENCONTRADO = "NO ENCONTRADO"
ESTADO_LETRA_PREPROCESADO = "LETRA PREPROCESADO"

NOMBRE_COLECCION_CANCIONES = "CANCIONES"

def insertarCancionCantante(elementosExtraidos):
    """
    Función que inserta una coleccion de de canciones y sus cantantes en BDD
    Argumentos:
        elementosExtraidos: arreglo de ranking, cancion y cantante
    Retorna: arrego de listas de canciones con el ranking y el identificador principal en BDD
    """
    try:
        log.info('Registra canciones en base de datos')
        # formatea los valores de ranking, canción y cantante en documento para el registro de la colección en MongoDB
        lista_canciones = []
        for elemento in elementosExtraidos:
            ranking, cancion, cantante = elemento
            # inserta colecciones de canciones en MongoDB
            cancion_id = mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_CANCIONES, {"cancion": cancion, "cantante": cantante, "estado": ESTADO_SIN_LETRA})
            # obtiene lista 
            lista_canciones.append({"ranking": ranking, "cancion_id": cancion_id})
        
        return lista_canciones
    except:
        log.error("Error al registrar canción: ", sys.exc_info()[0])

def obtenerCancionesPorEstado(estado):
    """
    Función que obtiene colección de canciones por estado
    Argumentos:
        estado: estado de la canción
    Retorna: colección de canciones
    """
    try:
        log.info('Obtiene canciones por estado: ' + estado)
        canciones_sin_letra = mongoDB_cliente.obtenerColeccion(NOMBRE_COLECCION_CANCIONES, {'estado': estado})   
        return canciones_sin_letra
    except:
        log.error("Error al obtenr canción de base de datos: ", sys.exc_info()[0])

def actualizarCancionPendiente(coleccion_cancion_pendiente, letra_cancion):
    """
    Función que actualiza una colección de cancion 
    Argumentos:
        coleccion_cancion_pendiente: objeto de tipo colección de canción
        letra_cancion: letra de la canción
    """
    if letra_cancion == '':
        return "La letra de canción es requerida"
    else:
        mongoDB_cliente.actualizarColeccion(NOMBRE_COLECCION_CANCIONES, coleccion_cancion_pendiente, 
            {"$set": {'letra': letra_cancion, 'estado': ESTADO_CON_LETRA}})
        return "documento actualizado correctamente"

def actualizarCancionNoEncontrado(coleccion_cancion_pendiente):
    """
    Función que actualiza una colección de cancion que no pudo obtener la letra 
    Argumentos:
        coleccion_cancion_pendiente: objeto de tipo colección de canción
    """
    mongoDB_cliente.actualizarColeccion(NOMBRE_COLECCION_CANCIONES, coleccion_cancion_pendiente, 
        {"$set": {'estado': ESTADO_NO_ENCONTRADO}})
    return "documento actualizado correctamente"

def actualizarCancionPreprocesado(coleccion_cancion_pendiente, letra_preprocesada):
    """
    Función que actualiza una colección de cancion con la letra depurada y preprocesada 
    Argumentos:
        coleccion_cancion_pendiente: objeto de tipo colección de canción
        letra_preprocesada: letra depurada y preprocesada
    """
    mongoDB_cliente.actualizarColeccion(NOMBRE_COLECCION_CANCIONES, coleccion_cancion_pendiente, 
        {"$set": {'estado': ESTADO_LETRA_PREPROCESADO, 'letra_preprocesada': letra_preprocesada}})
    return "documento actualizado correctamente"

def actualizarCancionSentimientoMultiple(coleccion_cancion_pendiente, clasificacion):
    """
    Función que actualiza una colección de cancion con el resultado de la clasificacion de sentimiento múltiple
    Argumentos:
        coleccion_cancion_pendiente: objeto de tipo colección de canción
        clasificacion: resultados de sentimiento múltiple
    """
    mongoDB_cliente.actualizarColeccion(NOMBRE_COLECCION_CANCIONES, coleccion_cancion_pendiente, 
        {"$set": {'sentimiento_multiple': clasificacion}})
    return "documento actualizado correctamente"

def actualizarCancionSentimientoBinario(coleccion_cancion_pendiente, sentimientoBinario):
    """
    Función que actualiza una colección de cancion con el resultado de la clasificacion de sentimiento binario
    Argumentos:
        coleccion_cancion_pendiente: objeto de tipo colección de canción
        sentimientoBinario: resultados de sentimiento binario
    """
    mongoDB_cliente.actualizarColeccion(NOMBRE_COLECCION_CANCIONES, coleccion_cancion_pendiente, 
        {"$set": {'sentimiento_binario': sentimientoBinario}})
    return "documento actualizado correctamente"
