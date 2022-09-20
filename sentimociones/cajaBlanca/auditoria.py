"""
Módulo auditoria.py

Implementación de lógica de negocio para canciones
"""
import sys
sys.path.append(sys.path[0] + '/..')
from bdd import mongoDB_cliente
from comun import fecha, cadena

NOMBRE_COLECCION_AUDITORIA = "AUDITORIA"

TIPO_AUDITORIA_PROCESO = 'Proceso'
TIPO_AUDITORIA_ML = 'Modelos Aprendizaje Automático'

ESTADO_COMPLETADO = 'COMPLETADO'
ESTADO_ERROR = 'ERROR'
RESULTADO_EXITO = 'resultado:exito'
RESULTADO_FRACASO = 'resultado:fracaso'

def registrarPistaProceso(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para procesos en mongo DB
    Argumentos:
        colección: arreglo de pista de auditoría
    """
    proceso, tiempo_inicio, caracteristicas = coleccion 
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_PROCESO, 
    "nombre": proceso, "fecha": fecha.obtenerFechaTiempoActual(), "duración": cadena.obtenertiempoProcesado(tiempo_inicio), "caracteristicas": caracteristicas})

def registrarPistaModelosML(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para modelos de aprendizaje automáticos
    Argumentos:
        colección: arreglo de pista de auditoría
    """
    modelo, proceso, tiempo_inicio, parametros, resultados = coleccion
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_ML, 
    "modelo": modelo, "fecha": fecha.obtenerFechaTiempoActual() , "proceso": proceso, "duración": cadena.obtenertiempoProcesado(tiempo_inicio), 
    "parametros": parametros, "resultados": resultados})
