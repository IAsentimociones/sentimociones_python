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

PROCESO_CLASIFICACION_SENTIMIENTO_MULTIPLE = 'Clasifiación Sentimientos Múltiples'
PROCESO_CLASIFICACION_SENTIMIENTO_BINARIO = 'Clasifiación Sentimientos Binario'

def registrarPistaProceso(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para procesos en mongo DB
    Argumentos:
        colección: arreglo de pista de auditoría
    """
    proceso, tiempo_inicio, caracteristicas = coleccion 
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_PROCESO, 
    "nombre": proceso, "fecha": fecha.obtenerFechaTiempoActual(), "duración": cadena.obtenertiempoProcesado(tiempo_inicio), "caracteristicas": caracteristicas})

def registrarPistaSentimientosMultiples(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para modelos de aprendizaje automáticos utilizado para la clasificación
    de sentimientos múltiples
    Argumentos:
        colección: arreglo de pista de auditoría con la siguiente estructura:
                    tiempo_inicio, cancion, cantante, modelo, para_resul
    """
    tiempo_inicio, cancion, cantante, modelo, para_resul = coleccion
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_ML, 
    "proceso": PROCESO_CLASIFICACION_SENTIMIENTO_MULTIPLE, "fecha": fecha.obtenerFechaTiempoActual() , 
    "duración": cadena.obtenertiempoProcesado(tiempo_inicio), 'canción': cancion, 'cantante': cantante,
    "modelo": modelo, "parametros y resultados": para_resul})

def registrarPistaSentimientosBinario(coleccion):
    """
    Función que inserta una pista en la colección de auditoría para modelos de aprendizaje automáticos utilizado para la clasificación
    de sentimientos binarios
    Argumentos:
        colección: arreglo de pista de auditoría con la siguiente estructura:
                    tiempo_inicio, cancion, cantante, modelo, para_resul
    """
    tiempo_inicio, cancion, cantante, modelo, para_resul = coleccion
    mongoDB_cliente.insertarDocumento(NOMBRE_COLECCION_AUDITORIA, {"tipo auditoria": TIPO_AUDITORIA_ML, 
    "proceso": PROCESO_CLASIFICACION_SENTIMIENTO_BINARIO, "fecha": fecha.obtenerFechaTiempoActual() , 
    "duración": cadena.obtenertiempoProcesado(tiempo_inicio), 'canción': cancion, 'cantante': cantante,
    "modelo": modelo, "parametros y resultados": para_resul})
