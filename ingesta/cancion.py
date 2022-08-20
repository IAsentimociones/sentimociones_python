"""
Módulo cancion.py

Implementación de lógica de negocio para canciones
"""
from bdd import mongoDB_cliente

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
        cancion_id = mongoDB_cliente.insertarDocumento("CANCIONES", {"cancion": cancion, "cantante": cantante})
        # obtiene lista 
        lista_canciones.append({"ranking": ranking, "cancion_id": cancion_id})
       
    return lista_canciones

