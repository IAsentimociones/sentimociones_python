"""
Módulo sentimientoMultiple.py

Implementa funciones para la clasificación de sentimientos múltiples como alegría, ira, etc
"""

ALEGRIA = "alegría"
MIEDO = "miedo"
IRA = "ira"
TRISTEZA = "tristeza"
DISGUSTO = "disgusto"
VERGUENZA = "vergüenza"
CULPA = "culpa"

JOY = 'joy'
FEAR = 'fear'
ANGER = 'anger'
SADNESS = 'sadness'
DISGUST = 'disgust'
SHAME = 'shame'
GUILT = 'guilt'

def obtenerResultadoPredicciones(modelos):
    """
    Función que retorna los resultados de las predicciones que almacenó la estructura de modelos
    Argumentos:
        modelos: modelos utilizados en las predicciones
    Retorna:
        lista de resultados con el recuento de las predicciones
    """
    clasificacion = {}
    for modelo in modelos:
        # se discrimina modelo SVC ya que no está prediciendo
        if ('SVC' != modelo):
            prediccion_res = modelos[modelo][2]['prediccion']
            if prediccion_res not in clasificacion:
                clasificacion[prediccion_res] = 1
            else:
                clasificacion[prediccion_res] += 1
    return clasificacion