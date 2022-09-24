"""
Módulo entrenamiento.py

Implementa funciones para el entrenamiento de modelos de aprendizaje automáticos
"""
from sklearn.metrics import accuracy_score
import time
import sys
sys.path.append(sys.path[0] + '/..')
from cajaBlanca import auditoria


def entrenar_probar (modelo, X_train, X_test, y_train, y_test):
    """
    Función que entrena y prueba modelos
    Argumentos:
        modelo: modelo de aprendizaje automatico
    Retorna: objeto del modelo con sus resultados
    """
    tiempo_inicio = time.time()
    evaluacion = {}
    param_resul = {}
    nombre_modelo = modelo.__class__.__name__

    modelo.fit(X_train, y_train)
   
    #registro de pista de auditoría para el entrenamiento del modelo
    evaluacion['Precisión entrenamiento'] = accuracy_score(y_train, modelo.predict(X_train))
    evaluacion['Precisión pruebas'] = accuracy_score(y_test, modelo.predict(X_test))
    param_resul[nombre_modelo] = [modelo.get_params(), evaluacion]
    auditoria.registrarPistaSentimientosMultiples([tiempo_inicio, "", "", nombre_modelo, param_resul[nombre_modelo]])

    return param_resul[nombre_modelo]