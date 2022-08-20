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