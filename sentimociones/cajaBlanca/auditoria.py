"""
Módulo auditoria.py

Implementación de lógica de negocio para canciones
"""
import sys
sys.path.append(sys.path[0] + '/..')
from bdd import mongoDB_cliente

NOMBRE_COLECCION_AUDITORIA = "AUDITORIA"

TIPO_AUDITORIA_PROCESO = 'Proceso'
TIPO_AUDITORIA_ML = 'Modelos Aprendizaje Automático'

def registrarPistaProceso(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para procesos en mongo DB
    Argumentos:
        colección: arreglo de pista de auditoría
    """
    proceso, fecha, duracion, caracteristicas = coleccion 
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_PROCESO, 
    "nombre": proceso, "fecha": fecha, "duracion": duracion, "caracteristicas": caracteristicas})

def registrarPistaModelosML(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para modelos de aprendizaje automáticos
    Argumentos:
        colección: arreglo de pista de auditoría
    """
    modelo, fecha, proceso, parametros, resultados = coleccion 
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_ML, 
    "modelo": modelo, "fecha": fecha, "proceso": proceso, "parametros": parametros, "resultados": resultados})
