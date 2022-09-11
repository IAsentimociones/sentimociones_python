"""
Módulo mongoDB_cliente.py

Establece una conexión con la base de datos MongoDB e implementa métodos CRUD
"""
from pymongo import MongoClient

def conectar():
    """
    Función que establece la conexión a la base de datos
    Argumentos:
    Retorna: objeto de base de datos conectada
    """
    cliente = MongoClient('localhost', 27017)
    base_datos = cliente['test']
       
    return base_datos

def insertarDocumento(coleccion, documento):
    """
    Función inserta un documento a una colección de base de datos
    Argumentos:
        coleccion: nombre de la coleccion
        documento: documento que se insertará en la coleccion de base de datos
    Retorna: identificador del documento insertado
    """
    base_datos = conectar()
    coleccion_db = base_datos[coleccion]
    resultado = coleccion_db.insert_one(documento)
    return resultado.inserted_id

def insertarDocumentos(coleccion, documentos):
    """
    Función inserta varios documentos a una colección de base de datos
    Argumentos:
        coleccion: nombre de la coleccion
        documentos: arreglo de varios documentos que se insertarán en la coleccion de base de datos
    Retorna: identificadores de los documentos insertados
    """
    base_datos = conectar()
    coleccion_db = base_datos[coleccion]
    resultado = coleccion_db.insert_many(documentos)
    return resultado.inserted_ids

def obtenerColeccion(nombre_coleccion, filtro):
    """
    Función que obtiene lista de canciones por cadena de atributos
    Argumentos:
        filtro: estado de la canción
    Retorna: listado de canciones
    """
    base_datos = conectar()
    coleccion_db = base_datos[nombre_coleccion]
    canciones = coleccion_db.find(filtro)
    #.limit(1) # quitar el limite para obtener todas las canciones sin letras
    return canciones

def actualizarColeccion(nombre_coleccion, coleccion, atributos):
    """
    Función que actualiza una colección existen con actuales o nuevos atributos 
    Argumentos:
        nombre_coleccion: nombre de la colección
        coleccion: objeto de la coleccion a modificar
        atributos: actuales o nuevos atributos con sus valores
    Retorna: identificadores de los documentos insertados
    """
    base_datos = conectar()
    coleccion_db = base_datos[nombre_coleccion]
    coleccion_db.update_one(coleccion, atributos)