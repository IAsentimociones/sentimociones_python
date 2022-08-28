"""
Módulo cancion.py

Implementación de lógica de negocio para canciones
"""
from bdd import mongoDB_cliente

ESTADO_SIN_LETRA = "SIN LETRA"
ESTADO_CON_LETRA = "SIN LETRA"
NOMBRE_COLECCION_CANCIONES = "CANCIONES"

def insertarCancionCantante(elementosExtraidos):
    """
    Función que inserta una coleccion de de canciones y sus cantantes en BDD
    Argumentos:
        elementosExtraidos: arreglo de ranking, cancion y cantante
    Retorna: arrego de listas de canciones con el ranking y el identificador principal en BDD
    """
    # formatea los valores de ranking, canción y cantante en documento para el registro de la colección en MongoDB
    lista_canciones = []
    for elemento in elementosExtraidos:
        ranking, cancion, cantante = elemento
        # inserta colecciones de canciones en MongoDB
        cancion_id = mongoDB_cliente.insertarDocumento("CANCIONES", {"cancion": cancion, "cantante": cantante, "estado": ESTADO_SIN_LETRA})
        # obtiene lista 
        lista_canciones.append({"ranking": ranking, "cancion_id": cancion_id})
       
    return lista_canciones

def obtenerCancionesPendientes():
    """
    Función que obtiene colección de canciones por estado
    Argumentos:
        estado: estado de la canción
    Retorna: colección de canciones
    """
    canciones_sin_letra = mongoDB_cliente.obtenerColeccion(NOMBRE_COLECCION_CANCIONES, {'estado': ESTADO_SIN_LETRA})
       
    return canciones_sin_letra

def actualizarCancionPendiente(coleccion_cancion_pendiente, letra_cancion):
    """
    Función que actualiza una colección de cancion 
    Argumentos:
        coleccion_cancion_pendiente: objeto de tipo colección de canción
        letra_cancion: letra de la canción
    """
    mongoDB_cliente.actualizarColeccion(NOMBRE_COLECCION_CANCIONES, coleccion_cancion_pendiente, 
        {"$set": {'letra': letra_cancion, 'estado': ESTADO_CON_LETRA}})
       
    return "documento actualizado correctamente"