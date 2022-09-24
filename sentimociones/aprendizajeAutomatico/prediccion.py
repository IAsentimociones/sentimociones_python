"""
Módulo prediccion.py

Implementa funciones para la predicción de modelos de aprendizaje automáticos
"""
import time
import sys
sys.path.append(sys.path[0] + '/..')
from cajaBlanca import auditoria
from preprocesamiento import tokenizacion


def predecirTexto (modelo, texto, vectorizador, modelos, cancion, cantante):
    """
    Función que utilizar un modelo de ML e invoca el método de predecir textos
    Argumentos:
        modelo: modelo de aprendizaje automatico
    Retorna: objeto del modelo con sus resultados
    """
    tiempo_inicio = time.time()
    print(tiempo_inicio)
    features = tokenizacion.crear_caracteristica(texto, nrange=(1, 4))
    features = vectorizador.transform(features)
    prediction = modelo.predict(features)[0]

    resultado = {}
    resultado['prediccion'] = prediction
    modelos[modelo.__class__.__name__].append(resultado)
    #print('Clasificación de sentimientos con ', modelo.__class__.__name__, ' : ', emoji_dict[prediction], modelos['SVC'][2])
    auditoria.registrarPistaSentimientosMultiples([tiempo_inicio, cancion, cantante, modelo.__class__.__name__, modelos[modelo.__class__.__name__]])

    return prediction, modelos