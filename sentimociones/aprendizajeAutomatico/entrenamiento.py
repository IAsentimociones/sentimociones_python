"""
Módulo entrenamiento.py

Implementa funciones para el entrenamiento de modelos de aprendizaje automáticos
"""
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import time
import sys
sys.path.append(sys.path[0] + '/..')
from cajaBlanca import auditoria


def entrenar_probar_accu_score (modelo, X_train, X_test, y_train, y_test, esBinario):
    """
    Función que entrena y prueba modelos registrando el resultado de la predicción
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
    if esBinario:
        auditoria.registrarPistaSentimientosBinario([tiempo_inicio, "", "", nombre_modelo, param_resul[nombre_modelo]])
    else:
        auditoria.registrarPistaSentimientosMultiples([tiempo_inicio, "", "", nombre_modelo, param_resul[nombre_modelo]])
        
    return param_resul[nombre_modelo]

def entrenar_cross_score (modelo, X_train, y_train, esBinario):
    """
    Función que entrena y prueba modelos registrando la validación de matriz cruzada
    Argumentos:
        modelo: modelo de aprendizaje automatico
    Retorna: objeto del modelo con sus resultados
    """
    tiempo_inicio = time.time()
    evaluacion = {}
    param_resul = {}
    nombre_modelo = modelo.__class__.__name__

    if 'GaussianNB' == nombre_modelo:
        modelo.fit(X_train.toarray(), y_train)
    else:
        modelo.fit(X_train, y_train)
   
    #registro de pista de auditoría para el entrenamiento del modelo
    if 'GaussianNB' == nombre_modelo:
        matriz_cruzada = cross_val_score(estimator=modelo, X=X_train.toarray(), y=y_train, cv=5, n_jobs=-1)
    else:
        matriz_cruzada = cross_val_score(estimator=modelo, X=X_train, y=y_train, cv=5, n_jobs=-1)
    evaluacion = {}
    cont = 0
    for m in matriz_cruzada:
        evaluacion['prediccion ' + str(cont)] = m
        cont = cont + 1

    param_resul[nombre_modelo] = [modelo.get_params(), evaluacion]
    if esBinario:
        auditoria.registrarPistaSentimientosBinario([tiempo_inicio, "", "", nombre_modelo, param_resul[nombre_modelo]])
    else:
        auditoria.registrarPistaSentimientosMultiples([tiempo_inicio, "", "", nombre_modelo, param_resul[nombre_modelo]])
        
    return param_resul[nombre_modelo]